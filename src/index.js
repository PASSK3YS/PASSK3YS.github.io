export default {
    async fetch(request, env) {
        const url = new URL(request.url);
        const path = url.pathname;
        const headers = {
            "Access-Control-Allow-Origin": "https://kieran.colfer.net",
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"
        };

        if (request.method === "OPTIONS") {
            return new Response(null, { headers });
        }

        if (request.method === "GET") {
            const count = await env.UPVOTES.get(path) || 0;
            return new Response(JSON.stringify({ count: parseInt(count) }), {
                headers: { ...headers, "Content-Type": "application/json" }
            });
        }

        if (request.method === "POST") {
            const clientIP = request.headers.get("cf-connecting-ip") || "";
            const ipHash = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(clientIP + path));
            const hashArray = Array.from(new Uint8Array(ipHash));
            const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
            
            const hasVoted = await env.UPVOTES.get(`vote_${hashHex}`);
            if (hasVoted) {
                return new Response(JSON.stringify({ error: "Already voted" }), {
                    status: 429,
                    headers: { ...headers, "Content-Type": "application/json" }
                });
            }

            let count = await env.UPVOTES.get(path) || 0;
            count = parseInt(count) + 1;
            
            await env.UPVOTES.put(path, count.toString());
            await env.UPVOTES.put(`vote_${hashHex}`, "1");

            return new Response(JSON.stringify({ count }), {
                headers: { ...headers, "Content-Type": "application/json" }
            });
        }

        return new Response("Not found", { status: 404, headers });
    }
};