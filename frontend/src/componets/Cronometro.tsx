import { useEffect, useState } from "react";

interface CronometroProps {
    dataAlvo: string; // Ex: "2025-05-15T10:00:00"
  }
  

export const Cronometro = ({ dataAlvo }: CronometroProps) => {
    const [tempoRestante, setTempoRestante] = useState({
        dias: "00",
        horas: "00",
        minutos: "00",
        segundos: "00",
      });
    
      useEffect(() => {
        const alvo = new Date(dataAlvo).getTime();
    
        const atualizarTempo = () => {
          const agora = new Date().getTime();
          const diferenca = alvo - agora;
    
          if (diferenca <= 0) {
            setTempoRestante({ dias: "00", horas: "00", minutos: "00", segundos: "00" });
            clearInterval(intervalo);
            return;
          }
    
          const dias = Math.floor(diferenca / (1000 * 60 * 60 * 24));
          const horas = Math.floor((diferenca % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
          const minutos = Math.floor((diferenca % (1000 * 60 * 60)) / (1000 * 60));
          const segundos = Math.floor((diferenca % (1000 * 60)) / 1000);
    
          setTempoRestante({
            dias: String(dias).padStart(2, "0"),
            horas: String(horas).padStart(2, "0"),
            minutos: String(minutos).padStart(2, "0"),
            segundos: String(segundos).padStart(2, "0"),
          });
        };
    
        const intervalo = setInterval(atualizarTempo, 1000);

        return () => clearInterval(intervalo);
    }, [dataAlvo]);

    return (
        <div className="bg-white rounded-b-3xl w-full h-auto flex flex-col items-center mb-5">
            <div className="flex flex-row justify-center items-center mt-2">
                <h1 className="text-black font-bold text-[14px]">PGL ASTANA <span className="text-amber-600">começa em:</span></h1>
            </div>
            <div className="flex flex-row text-black p-2 gap-5">
                <div className="flex flex-col gap-1 justify-center items-center">
                    <span className="text-2xl font-bold">{tempoRestante.dias}</span> 
                    <span className="text-[12px] font-bold text-amber-800">Dias</span> 
                </div>

                <div className="flex flex-col gap-1 justify-center items-center">
                    <span className="text-2xl font-bold">{tempoRestante.horas}</span> 
                    <span className="text-[12px] font-bold text-amber-800">Horas</span> 
                </div>

                <div className="flex flex-col gap-1 justify-center items-center">
                    <span className="text-2xl font-bold">{tempoRestante.minutos}</span> 
                    <span className="text-[12px] font-bold text-amber-800">Miutos</span> 
                </div>

                <div className="flex flex-col gap-1 justify-center items-center">
                    <span className="text-2xl font-bold">{tempoRestante.segundos}</span> 
                    <span className="text-[12px] font-bold text-amber-800">Secundos</span> 
                </div>

            </div>
        </div>
    );
}