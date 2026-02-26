type Props = {
  total: number;
  conformes: number;
};

export default function ChecklistSummary({ total, conformes }: Props) {
  const score = total === 0 ? 0 : Math.round((conformes / total) * 100);

  return (
    <div className="mt-6 p-4 border rounded bg-gray-100">
      <h2 className="font-bold">Résultat</h2>
      <p>Conformes : {conformes} / {total}</p>
      <p>Score : {score} %</p>
    </div>
  );
}