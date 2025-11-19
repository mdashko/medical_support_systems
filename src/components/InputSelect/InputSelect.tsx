import "./InputSelect.scss";
import { SlArrowDown } from "react-icons/sl";
import { useState } from "react";

const options = [
    "Cough",
    "Fever",
    "Headache",
    "Sore throat",
    "Fatigue"
];


export const InputSelect = () => {
    const [value, setValue] = useState("");
    const [open, setOpen] = useState(false);

    return (
        <div className="input-select-container">
            <input
                className="input-select-container_input"
                type="text"
                value={value}
                placeholder="Choose symptoms..."
                onFocus={() => setOpen(true)}
                onChange={(e) => {
                    setValue(e.target.value);
                    setOpen(true);
                }}
            />

            <SlArrowDown className="input-select-container_icon" />

            {open && (
                <ul className="input-select-container_dropdown">
                    {options
                        .filter((item) =>
                            item.toLowerCase().includes(value.toLowerCase())
                        )
                        .map((item) => (
                            <li
                                key={item}
                                onClick={() => {
                                    setValue(item);
                                    setOpen(false);
                                }}
                            >
                                {item}
                            </li>
                        ))}
                </ul>
            )}
        </div>
    );
};