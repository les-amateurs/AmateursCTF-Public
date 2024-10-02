"use strict";
let beeFn = null;
const actions = ["U", "D", "L", "R", "I"];

this.onmessage = (e) => {
  if (e.data.type === "init") {
    initBee(e);
  } else if (e.data.type === "tick") {
    tickBee(e);
  }
};

const initBee = (e) => {
  beeFn = (world, me) =>
    new Function(...actions, "world", "me", e.data.code).apply(
      Object.create(null),
      [...actions.keys(), world, me]
    );
};

const tickBee = (e) => {
  try {
    const action = beeFn(e.data.world, e.data.me);
    postMessage({ type: "action", action });
  } catch (err) {
    postMessage({
      type: "error",
      msg: `<span class="text-red-500">&gt; A bee has crashed! ${err.toString()}</span>`,
    });
  }
};
