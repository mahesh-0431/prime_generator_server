import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
    const [start, setStart] = useState('');
    const [end, setEnd] = useState('');
    const [strategy, setStrategy] = useState('mahi');
    const [primes, setPrimes] = useState([]);
    const [elapsed,settime] = useState(null);
    const [len,setlen] = useState(null);

    const generatePrimes = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:8000/generate_primes/?start=${start}&end=${end}&strategy=${strategy}`);
            setPrimes(response.data.primes);
            settime(response.data.time);
            setlen(response.data.length);
        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <div>
            <h2>Prime Number Generator</h2>
            <div>
                <label>Start: </label>
                <input type="number" value={start} onChange={(e) => setStart(e.target.value)} />
            </div>
            <div>
                <label>End: </label>
                <input type="number" value={end} onChange={(e) => setEnd(e.target.value)} />
            </div>
            <div>
                <label>Strategy: </label>
                <select value={strategy} onChange={(e) => setStrategy(e.target.value)}>
                    <option value="prime">prime</option>
                    <option value="mahi">mahi</option>
                </select>
            </div>
            <button onClick={generatePrimes}>Generate Primes</button>
            <div>
                <h3>Primes: </h3>
                <ul>
                    {primes.map((prime, index) => (
                        <li key={index}>{prime}</li>
                    ))}
                </ul>
            </div>
            {elapsed && <p>time taken:{elapsed}</p>}
            {len && <p>number of primes:{len}</p>}
        </div>
    );
};

export default App;
