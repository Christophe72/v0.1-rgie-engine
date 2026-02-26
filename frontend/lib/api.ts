export async function fetchRules() {
  const res = await fetch("http://localhost:8000/rules", {
    cache: "no-store"
  });

  if (!res.ok) {
    throw new Error("Erreur API");
  }

  return res.json();
}