import { API_URL } from "../utils/api_urls";

export async function fetchListOfSymptoms() {
	const response = await fetch(`${API_URL}/symptoms`);

	if (!response.ok) {
		throw new Error("Failed to fetch symptoms");
	}

	const data = await response.json();
	return data.symptoms;
}

export async function sendListOfSymptoms(symptoms: string[]) {
	try {
		const res = await fetch(`${API_URL}/process-symptoms`, {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({ symptoms }),
		});

		const data = await res.json();
		return data; 
	} catch (err) {
		console.error("FETCH ERROR:", err);
	}
}


