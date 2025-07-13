import { useState } from 'react'
import axios from 'axios'

export default function App() {
  const [features, setFeatures] = useState({ danceability: '', valence: '', energy: '' })
  const [result, setResult] = useState<number | null>(null)

  const api = import.meta.env.VITE_API_URL || 'http://localhost:8000'

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFeatures({ ...features, [e.target.name]: e.target.value })
  }

  const predict = async () => {
    const res = await axios.post(`${api}/predict`, {
      danceability: parseFloat(features.danceability),
      valence: parseFloat(features.valence),
      energy: parseFloat(features.energy),
    })
    setResult(res.data.predicted_popularity)
  }

  return (
    <div className="min-h-screen bg-gray-100 py-12 px-4 flex flex-col items-center">
      <h1 className="text-4xl font-bold text-gray-800 mb-6">🎵 Hit Predictor</h1>

      <div className="bg-white shadow-md rounded-lg p-6 w-full max-w-md space-y-4">
        {['danceability', 'valence', 'energy'].map((field) => (
          <input
            key={field}
            name={field}
            type="number"
            placeholder={field}
            value={(features as any)[field]}
            onChange={handleChange}
            className="w-full border px-4 py-2 rounded text-sm"
          />
        ))}
        <button
          onClick={predict}
          className="bg-blue-600 text-white w-full py-2 rounded hover:bg-blue-700"
        >
          Predict
        </button>
      </div>

      {result !== null && (
        <div className="mt-8 bg-green-100 text-green-800 px-6 py-4 rounded shadow">
          🎯 Predicted Popularity: <span className="font-bold text-lg">{result}</span>
        </div>
      )}
    </div>
  )
}
