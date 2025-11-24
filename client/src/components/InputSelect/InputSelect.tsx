import { useState } from "react";
import { SlArrowDown } from "react-icons/sl";
import "./InputSelect.scss";

interface InputProps {
    value: string;
    illnesses: string[];
    onChange: (value: string) => void;
}

export const InputSelect: React.FC<InputProps> = ({ value, illnesses, onChange }) => {
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
                    onChange(e.target.value);
                    setOpen(true);
                }}
            />

            <SlArrowDown className="input-select-container_icon" />

            {open && (
                <ul className="input-select-container_dropdown">
                    {illnesses
                        .filter((item) =>
                            item.toLowerCase().includes(value.toLowerCase())
                        )
                        .map((item) => (
                            <li
                                key={item}
                                onClick={() => {
                                    onChange(item);
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
