// general imports
import React from 'react';
import { useSocket } from './hooks/useSocket';

// style imports
import './App.css';
import { ExchangeCard } from './components/ExchangeCard/ExchangeCard';

const App = () => {
    const { priceData, token, setToken } = useSocket();

    return (
        <div className="app-container">
            <div className="form-container">
                <div className="token-picker-container">
                    <select
                        name="token"
                        id="token"
                        value={token}
                        onChange={(e) => setToken(e.target.value)}
                    >
                        <option value="MATIC">MATIC</option>
                        <option value="DAI">DAI</option>
                        <option value="USDC">USDC</option>
                        <option value="USDT">USDT</option>
                    </select>
                </div>
            </div>
            <div className="card-container">
                {priceData.map((exchange, index) => {
                    return (
                        <ExchangeCard
                            key={index}
                            name={exchange.exchange_name}
                            price={exchange.current_price}
                        />
                    );
                })}
            </div>
        </div>
    );
};

export default App;
