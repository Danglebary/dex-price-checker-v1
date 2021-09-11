import { io, Socket } from 'socket.io-client';
import { DefaultEventsMap } from 'socket.io-client/build/typed-events';

const endPoint = 'ws://localhost:4000';
let socket: Socket<DefaultEventsMap, DefaultEventsMap>;

export const initSocketConnection = () => {
    socket = io(endPoint);
    console.log('[CLIENT] Socket connecting...');
    socket.on('error', (err) => {
        console.log(`[CLIENT] Connection error has occured : ${err}`);
    });
};

export const disconnectSocket = () => {
    if (socket) socket.disconnect();
    console.log('[CLIENT] Socket disconnected');
};

export const queryPriceData = (dataToSend: any, cb: any) => {
    if (!socket) {
        return cb(true);
    } else {
        socket.emit('price_data_query', dataToSend);

        socket.on('price_data_response', (msg) => {
            setTimeout(() => {
                socket.emit('price_data_query', dataToSend);
            }, 5000);
            return cb(null, msg);
        });
    }
};
