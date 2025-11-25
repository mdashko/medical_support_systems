import { Container } from "react-bootstrap";
import "./Main.scss";
import { InputSelect } from "../InputSelect/InputSelect";
import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { AppDispatch } from "../../state-managment/store";
import { addSymptom, removeSymptom } from "../../state-managment/actions";
import { RootState } from "../../state-managment/store";
import { fetchListOfSymptoms, sendListOfSymptoms } from "../../services/systemService";

const Main: React.FC = () => {
	const [symptomValue, setSymptomValue] = useState("");
	const [listOfSymptoms, setListOfSymptoms] = useState<string[]>([]);
	const [loading, setLoading] = useState(true);
	const dispatch = useDispatch<AppDispatch>();

	const symptoms = useSelector((state: RootState) => state.symptoms);

	useEffect(() => {
		fetchListOfSymptoms()
			.then((list) => setListOfSymptoms(list))
			.finally(() => setLoading(false));
	}, []);
	const onAdd = () => {
		if (!symptomValue.trim()) {
			return;
		}

		if (symptoms.includes(symptomValue)) {
			return;
		}

		dispatch(addSymptom(symptomValue));
		setSymptomValue("");
	};

	const onRemove = (
		event: React.MouseEvent<HTMLDivElement>,
		symptom: string
	) => {
		if (symptoms.includes(symptom) === false) {
			return;
		}

		dispatch(removeSymptom(symptom));
	};

	const startAnalysis = () => {
		sendListOfSymptoms(symptoms);
	};

	function renderIllnessInput() {
		switch (loading) {
			case true:
				return <p>Loading symptoms...</p>;

			case false:
				return (
					<div className="main-content">
						<section className="main-content__setup-section">
							<div className="main-content__setup-section__input-container">
								<InputSelect
									value={symptomValue}
									symptoms={listOfSymptoms}
									onChange={setSymptomValue}
								/>
								<button
									className="main-content__setup-section__input-container_button"
									onClick={onAdd}
								>
									Add
								</button>
							</div>
							<div className="main-content__setup-section__input-container__symptoms-container">
								{symptoms.map((item, i) => (
									<div
										className="main-content__setup-section__input-container__symptoms-container__symptom-bubble"
										key={i}
										onClick={(event) => onRemove(event, item)}
									>
										{item}
									</div>
								))}
							</div>
							<button className="main-content__setup-section__button" onClick={startAnalysis}>
								Start Analysis
							</button>
						</section>

						<section className="main-content__result-section">
							<textarea
								name=""
								id=""
								className="main-content__result-section__result-textarea"
							></textarea>
						</section>
					</div>
				);

			default:
				return null;
		}
	}

	return (
		<Container className="">
			<div>
				<header></header>
				{renderIllnessInput()}

				<footer className=""></footer>
			</div>
		</Container>
	);
};

export default Main;
