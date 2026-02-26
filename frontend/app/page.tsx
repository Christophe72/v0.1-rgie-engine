interface Rule {
  id: string | number;
  code: string;
  title: string;
}

async function getRules(): Promise<Rule[]> {
  const apiBaseUrl = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";
  const res = await fetch(`${apiBaseUrl}/rules`, {
    cache: "no-store"
  });
  return res.json();
}

export default async function Home() {
  const rules = await getRules();

  return (
    <main className="p-6">
      <h1 className="text-xl font-bold mb-4">RGIE Rules</h1>
      <ul>
        {rules.map((rule: Rule) => (
          <li key={rule.id}>
            {rule.code} - {rule.title}
          </li>
        ))}
      </ul>
    </main>
  );
}