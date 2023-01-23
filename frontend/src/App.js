import logo from "./logo.svg";
import axios from "axios";
import "./App.css";
import { useEffect, useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
function App() {
  const [countries, setCountries] = useState([]);
  const [selectedCountry, setSelectedCountry] = useState("");
  const [genders, setGenders] = useState([]);
  const [selectedGender, setSelectedGender] = useState("");
  // const [isShown, setIsShown] = useState(true);

  const fetchData = async (gender, country) => {
    try {
      if (gender == "" && country != "") {
        const response = await axios.get(
          `http://127.0.0.1:8000/name/noGender/${country}`
        );
        return response.data;
      } else {
        const response = await axios.get(
          `http://127.0.0.1:8000/name/${gender}/${country}`
        );
        return response.data;
      }
    } catch (error) {
      console.error(error);
    }
  };

  const handleClick = (event) => {
    const gender = selectedGender;
    const country = selectedCountry;
    var element = document.getElementById("randomName");
    const nameData = fetchData(gender, country)
      .then((data) => (element.innerText = data))
      .then((data) => console.log(data))
      .catch((error) => console.log(error));
  };
  useEffect(() => {
    fetch("http://127.0.0.1:8000/countries")
      .then((response) => response.json())
      .then((data) => setCountries(data));
  }, []);

  const handleChange = (event) => {
    setSelectedCountry(event.target.value);
  };

  const options = countries.map((country) => (
    <option key={country} value={country}>
      {country}
    </option>
  ));

  useEffect(() => {
    fetch("http://127.0.0.1:8000/genders")
      .then((response) => response.json())
      .then((data) => setGenders(data));
  }, []);
  const handleChangeGender = (event) => {
    setSelectedGender(event.target.value);
  };
  const genderOptions = genders.map((gender) => (
    <option key={gender} value={gender}>
      {gender}
    </option>
  ));
  return (
    <div align='center'>
      <h1>Random Name Generator</h1>
      <br></br>
      <h2>Gender</h2>
      <select value={selectedGender} onChange={handleChangeGender}>
        {genderOptions}
      </select>
      <br></br>
      <br></br>
      <h2>Country</h2>
      <select value={selectedCountry} onChange={handleChange}>
        {options}
      </select>
      <br></br>
      <br></br>
      <button onClick={handleClick}>Generate</button>
      <div>
        <br></br>
        <br></br>
        <h2 id='randomName' className='h2'></h2>
      </div>
    </div>
  );
}

export default App;
