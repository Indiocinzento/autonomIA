// frontend/pages/api/proxy.js
// Evita problemas de CORS durante desenvolvimento

export default async function handler(req, res) {
  const { url } = req.query;
  const targetUrl = `http://backend:8000${url}`;
  
  try {
    const response = await fetch(targetUrl);
    const data = await response.json();
    res.status(200).json(data);
  } catch (error) {
    res.status(500).json({ erro: "Backend não encontrado", mensagem: error.message });
  }
}
