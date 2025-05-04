"use client"

import {useRef, useState } from "react";

export const Chat = () => {

    const chatBoxRef = useRef<HTMLDivElement>(null);
    const [inputValor, SetInputValor] = useState<string>('');

    const pegaCampoInput = (valor: React.ChangeEvent<HTMLInputElement>) => {
        SetInputValor(valor.target.value); 
    }

    const teclaPress = (evento: React.KeyboardEvent<HTMLInputElement>) => {
        if(evento.key === 'Enter'){sendMessage();}
    }

    const updateMessage = (messageDiv: HTMLDivElement, newText: string, sender: string) => {
        messageDiv.innerText = `${sender}: ${newText}`;
      }


    async function sendMessage() {
        const userInput = inputValor.trim();
        if (!userInput) return;
      
        showMessage('Você', userInput);
        const loadingMessageId = showMessage('Fã FURIA Bot', 'Digitando...');
      
        try {
            const response = await fetch('https://desafiofuria.zantech.com.br/webhook', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: userInput })
          });
      
            const data = await response.json();
            if(loadingMessageId){
                updateMessage(loadingMessageId, data.reply, 'Fã Furia Bot');
            }
            SetInputValor('');
        } catch (error) {
          console.error('Erro ao enviar mensagem:', error);
          if(loadingMessageId){
            updateMessage(loadingMessageId, 'Ocorreu um erro ao tentar falar com o servidor.', 'Fã Furia Bot');
          }
        }
      }
      
    const showMessage = (sender: string, message: string): HTMLDivElement | null => {

        const chatBox = chatBoxRef.current;
        if(!chatBox) return null;
      
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message');
      
        if (sender === 'Você') {
          messageDiv.className = 'max-w-[70%] self-end bg-green-200 text-black text-right p-3 rounded-lg mb-2';
          
        } else {
          messageDiv.className = 'max-w-[70%] self-start bg-gray-700 text-white text-left p-3 rounded-lg mb-2';
        }
      
        messageDiv.innerText = `${sender}: ${message}`;
        chatBox.appendChild(messageDiv);
      
        // Scroll automático para o final
        if(chatBox){
            chatBox.scrollTop = chatBox.scrollHeight;
        }

        return messageDiv;
        
    }


    return (
        <div className="h-auto bg-black text-white font-sans">
            <style>

            </style>
            <main className="flex flex-col items-center justify-center">
                <div id="chat-container" className="flex flex-col h-[calc(100vh-160px)] max-w-3xl w-full mx-auto p-4">
                    <div id="chat-box" ref={chatBoxRef} className="flex flex-col flex-1 overflow-y-auto border border-gray-700 p-4 bg-gray-900 rounded-lg mb-4">
                   
                    </div>
                    <div id="input-container" className="flex">
                        <input
                        type="text"
                        id="user-input"
                        onChange={pegaCampoInput}
                        onKeyDown={teclaPress}
                        value={inputValor}
                        placeholder="Digite sua mensagem..."
                        className="flex-1 p-3 text-base rounded-md mr-2 text-black bg-white"
                        />
                        <button
                        id="send-btn"
                        type="button"
                        onClick={sendMessage}
                        className="px-5 py-3 text-base bg-pink-600 text-white rounded-md hover:bg-pink-700 transition-colors"
                        >
                        Enviar
                        </button>
                    </div>
                </div>
            </main>
        </div>

    );
}