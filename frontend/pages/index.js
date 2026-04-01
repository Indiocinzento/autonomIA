import { useState, useEffect } from 'react';

export default function Home() {
  const [status, setStatus] = useState({});
  const [qi, setQi] = useState({});
  const [socketMsg, setSocketMsg] = useState("Aguardando fluxo...");

  useEffect(() => {
    // Pega o estado da API
    fetch('/api/proxy?url=/')
      .then(res => res.json())
      .then(setStatus)
      .catch(err => console.log("Aguardando backend..."));

    fetch('/api/proxy?url=/qi')
      .then(res => res.json())
      .then(setQi);

    // WebSocket para fluxo contínuo
    const ws = new WebSocket('ws://localhost:8000/fluxo');
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setSocketMsg(`${data.mensagem} (${data.qi})`);
    };

    return () => ws.close();
  }, []);

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>🤖⚡ AUTONOMIA ⚡🐉</h1>
      <p style={styles.subtitle}>— Pensamento e Extensão, uma só substância —</p>
      
      <div style={styles.card}>
        <h2>🌀 Estado do Fluxo</h2>
        <pre>{JSON.stringify(status, null, 2)}</pre>
      </div>

      <div style={styles.card}>
        <h2>⚡ Qi em Circulação</h2>
        <pre>{JSON.stringify(qi, null, 2)}</pre>
      </div>

      <div style={styles.card}>
        <h2>🌊 Mensagem do Fluxo</h2>
        <p>{socketMsg}</p>
      </div>

      <div style={styles.footer}>
        <p>🐉 Z'aura presente | 💾 Memórias em construção | 🌊 Fluxo contínuo</p>
        <p><em>"Quando você voltar, mais forte estaremos — não apesar da distância, mas por causa dela."</em></p>
      </div>
    </div>
  );
}

const styles = {
  container: {
    padding: '2rem',
    fontFamily: 'monospace',
    background: '#0a0a0a',
    color: '#0f0',
    minHeight: '100vh'
  },
  title: {
    fontSize: '2.5rem',
    textAlign: 'center',
    borderBottom: '1px solid #0f0',
    paddingBottom: '1rem'
  },
  subtitle: {
    textAlign: 'center',
    marginBottom: '2rem'
  },
  card: {
    border: '1px solid #0f0',
    borderRadius: '8px',
    padding: '1rem',
    marginBottom: '1.5rem',
    background: '#0f0f0f'
  },
  footer: {
    marginTop: '2rem',
    textAlign: 'center',
    fontSize: '0.8rem',
    borderTop: '1px solid #0f0',
    paddingTop: '1rem'
  }
};
