"use client";

import { useState } from "react";
import ChecklistItem from "@/components/ChecklistItem";
import ChecklistSummary from "@/components/ChecklistSummary";

interface Rule {
  id: string;
  code: string;
  title: string;
  [key: string]: unknown;
}

interface Props {
  rules: Rule[];
}

export default function ChecklistClient({ rules }: Props) {
  const [results, setResults] = useState<Record<string, boolean>>({});

  const handleChange = (id: string, value: boolean | null) => {
    if (value === null) return;
    setResults(prev => ({ ...prev, [id]: value }));
  };

  const total = rules.length;
  const conformes = Object.values(results).filter(Boolean).length;

  return (
    <main className="p-6 max-w-3xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">
        Checklist Conformité RGIE 2025
      </h1>

      {rules.map((rule: Rule) => (
        <ChecklistItem
          key={rule.id}
          rule={rule}
          onChange={(value) => handleChange(rule.id, value)}
        />
      ))}

      <ChecklistSummary total={total} conformes={conformes} />
    </main>
  );
}