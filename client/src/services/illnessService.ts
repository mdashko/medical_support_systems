import { API_URL } from "../utils/api_urls";

export async function fetchListOfIllnesses() {
  const response = await fetch(`${API_URL}/illnesses`);

  if (!response.ok) {
    throw new Error("Failed to fetch illnesses");
  }

  const data = await response.json();
  return data.illnesses; 
}
