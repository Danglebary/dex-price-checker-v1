// general imports
import React from 'react';

// style import
import './exchangeCard.css';

interface Props {
    name: string;
    price: string;
}

export const ExchangeCard = ({ name, price }: Props) => {
    return (
        <div className="exchange-card-container">
            <div className="exchange-name">{name}</div>
            <div className="exchange-price">{price}</div>
        </div>
    );
};
