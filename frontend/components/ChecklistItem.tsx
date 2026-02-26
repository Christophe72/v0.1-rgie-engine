"use client";

import { useState } from "react";
import { Rule } from "@/types/rule";

type Props = {
  rule: Rule;
  onChange: (value: boolean | null) => void;
};

export default function ChecklistItem({ rule, onChange }: Props) {
  const [status, setStatus] = useState<boolean | null>(null);

  const handleSelect = (value: boolean) => {
    setStatus(value);
    onChange(value);
  };

  return (
    <div className="border rounded p-4 mb-3">
      <h3 className="font-semibold">
        {rule.code} - {rule.title}
      </h3>
      <p className="text-sm text-gray-600 mb-2">{rule.description}</p>

      <div className="flex gap-4">
        <button
          onClick={() => handleSelect(true)}
          className={`px-3 py-1 rounded ${
            status === true ? "bg-green-600 text-white" : "bg-gray-200"
          }`}
        >
          Conforme
        </button>

        <button
          onClick={() => handleSelect(false)}
          className={`px-3 py-1 rounded ${
            status === false ? "bg-red-600 text-white" : "bg-gray-200"
          }`}
        >
          Non conforme
        </button>
      </div>
    </div>
  );
}