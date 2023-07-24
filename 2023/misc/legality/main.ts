import { serve } from "https://deno.land/std@0.181.0/http/server.ts";
import { serveFile } from "https://deno.land/std@0.181.0/http/file_server.ts";

const handler = async (request: Request): Promise<Response> => {
  const url = new URL(request.url);
  switch(url.pathname) {
    case "/":
        return await serveFile(request, "index.html");
    case "/LICENSE":
        return await serveFile(request, "LICENSE");
    case "/submit":
        if(url.searchParams.get("password") == "il0vefreesoftware!distributefreely!") {
            return await serveFile(request, "flag.txt");
        } else {
            return new Response("incorrect password.")
        }
  }

  return await serveFile(request, "404.html");
};

await serve(handler);