import { Container } from "react-bootstrap";
import "./Main.scss";
import { SlArrowDown } from "react-icons/sl";
import { InputSelect } from "../InputSelect/InputSelect";


const Main: React.FC = () => {
  return (
    <Container className="">
      <header>

      </header>
      <div className="main-content">
        <section className="main-content__setup-section">
          <div className="main-content__setup-section__input-container">
            {/* <input className="main-content__setup-section__input-container_input" type="text" placeholder="Choose symptoms...." />
            <SlArrowDown className="main-content__setup-section__input-container_icon" /> */}
            <InputSelect />
          </div>


          <button className="main-content__setup-section__button">Start Analysis</button>
        </section>

        <section className="main-content__result-section">
          <textarea name="" id="" className="main-content__result-section__result-textarea"></textarea>

        </section>
      </div>
      <footer className="">

      </footer>
    </Container>
  );
};

export default Main;