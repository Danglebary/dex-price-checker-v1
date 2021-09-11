import { useState, useEffect } from 'react';
import {
    disconnectSocket,
    initSocketConnection,
    queryPriceData
} from './socket.service';

type PriceData = {
    exchange_name: string;
    current_price: string;
};

export const useSocket = () => {
    const [priceData, setPriceData] = useState([] as PriceData[]);
    const [exchanges, setExchanges] = useState([
        'SUSHISWAP',
        'APESWAP',
        'POLYCAT',
        'QUICKSWAP',
        'GRAVITY'
    ]);
    const [token, setToken] = useState('MATIC');

    useEffect(() => {
        initSocketConnection();

        const dataToSend = { exchanges: exchanges, token: token };

        queryPriceData(dataToSend, (err: boolean, data: any) => {
            if (err) {
                console.log('[CLIENT] Connection error has occured');
            } else {
                setPriceData(data.data);
            }
        });

        return () => {
            disconnectSocket();
        };
    }, [exchanges, token]);

    return {
        priceData,
        exchanges,
        setExchanges,
        token,
        setToken
    };
};
