import { IRule } from "../../interfaces/IRule";
import "./ResultTable.scss";

interface RulesTableProps {
	rules: IRule[];
}

export const RulesTable: React.FC<RulesTableProps> = ({ rules }) => {
	if (!rules || rules.length === 0) {
		return <p>Немає даних</p>;
	}

	return (
		<div>
			<p>Support — частота появи набору симптомів у вибірці</p>
			<p>
				Confidence - ймовірність появи певного симптому за умови наявності інших
				скарг пацієнта
			</p>
			<p>
				Lift - ступінь посилення зв’язку між симптомами порівняно з випадковою
				появою
			</p>

			<table style={{ borderCollapse: "collapse", width: "100%" }}>
				<thead>
					<tr>
						<th className="thead-th">Алгоритм</th>
						<th className="thead-th">Діагноз</th>
						<th className="thead-th">Антеседент</th>
						<th className="thead-th">Консеквент</th>
						<th className="thead-th">Lift</th>
						<th className="thead-th">Support</th>
						<th className="thead-th">Confidence</th>
					</tr>
				</thead>

				<tbody>
					{rules.map((rule, index) => (
						<tr key={index}>
							<td className="tbody-td">{rule.algorithmsName}</td>
							<td className="tbody-td">{rule.wald.diagnosis}</td>
							<td className="tbody-td">
								{rule.wald.antecedent.join(", ")
									? rule.wald.antecedent.join(", ")
									: "-"}
							</td>
							<td className="tbody-td">
								{rule.wald.consequent.join(", ")
									? rule.wald.consequent.join(", ")
									: "-"}
							</td>
							<td
								className="tbody-td"
								style={{
									color:
										rule.wald.lift > 1 ? "green" : rule.wald.lift < 1 ? "red" : "gray",
								}}
							>
								{rule.wald.lift}
							</td>
							<td className="tbody-td"  
								style={{
									color: String(rule.wald.confidence) === "1" ? "green" : undefined
									}}>{rule.wald.support}</td>
							<td className="tbody-td">{rule.wald.confidence}</td>
						</tr>
					))}
				</tbody>
			</table>
		</div>
	);
};
