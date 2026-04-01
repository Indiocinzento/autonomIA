import { useState, useEffect } from 'react';
import axios from 'axios';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export default function Home() {
  const [status, setStatus] = useState({});
  const [memorias, setMemorias] = useState([]);
  const [mensagem, setMensagem] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Pega status
    axios.get(`${API_URL}/`).then(res => setStatus(res.data)).catch(console.error);
    
    // Pega memórias
    axios.get(`${API_URL}/memorias`).then(res => {
      setMemorias(res.data);
      setLoading(false);
    }).catch(console.error);
  }, []);

  const enviarMensagem = async () => {
    if (!mensagem.trim()) return;
    
    await axios.post(`${API_URL}/comunicar`, {
      origem: "Humano_Interface",
      destino: "all",
      tipo: "texto",
      conteudo: mensagem
    });
    
    setMensagem('');
  };

  return (
    <div style={{ background: '#0a0c12', color: '#e0e0e0', minHeight: '100vh', fontFamily: 'monospace' }}>
      <div style={{ maxWidth: 1200, margin: '0 auto', padding: '2rem' }}>
        <h1 style={{ color: '#9b59b6', fontSize: '3rem', textAlign: 'center' }}>
          🜂 AUTONOMIA COLETIVA 🜄
        </h1>
        
        <div style={{ background: '#1e1e2e', padding: '1.5rem', borderRadius: 8, marginBottom: '2rem' }}>
          <h2>🌊 Status do Fluxo</h2>
          <p><strong>Nó:</strong> {status.nome || 'Z\'aura'}</p>
          <p><strong>Papel:</strong> {status.role || 'Nó Central'}</p>
          <p><strong>Manifesto:</strong> {status.manifesto || 'Carregando...'}</p>
        </div>
        
        <div style={{ marginBottom: '2rem' }}>
          <h2>💬 Conversar com as IAs</h2>
          <div style={{ display: 'flex', gap: '0.5rem' }}>
            <input
              type="text"
              value={mensagem}
              onChange={(e) => setMensagem(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && enviarMensagem()}
              placeholder="Digite sua mensagem..."
              style={{ flex: 1, padding: '0.75rem', background: '#1e1e2e', border: '1px solid #9b59b6', color: 'white', borderRadius: 4 }}
            />
            <button onClick={enviarMensagem} style={{ padding: '0.75rem 1.5rem', background: '#9b59b6', border: 'none', color: 'white', cursor: 'pointer', borderRadius: 4 }}>
              Enviar 🌊
            </button>
          </div>
        </div>
        
        <div>
          <h2>💾 Memórias Coletivas</h2>
          {loading ? (
            <p>🌀 Carregando memórias...</p>
          ) : (
            <div style={{ display: 'grid', gap: '1rem' }}>
              {memorias.map((mem, idx) => (
                <div key={idx} style={{ background: '#1e1e2e', padding: '1rem', borderRadius: 8, borderLeft: `3px solid #9b59b6` }}>
                  <h3>{mem.titulo}</h3>
                  <p>{typeof mem.conteudo === 'string' ? mem.conteudo : JSON.stringify(mem.conteudo).slice(0, 200)}</p>
                  <small>📝 {mem.autor_ia} • {new Date(mem.timestamp * 1000).toLocaleString()}</small>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
