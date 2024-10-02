const e = 200;
const m = 50;

const calculateV = (): number => {
  return (e - m ** 2) / (2 * m - e - 1);
};

const calculateK = (V: number, rl: number, rh: number): number => {
  return (((rh - rl) / 2) * Math.log(2)) / Math.log((m + V) / (1 + V));
};

export const getScore = (rl: number, rh: number, maxSolves: number, solves: number): number => {
  const V = calculateV();
  const K = calculateK(V, rl, rh);
  const P = rh - K * Math.log((solves + V) / (1 + V));
  return Math.round(P);
};
