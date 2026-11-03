from flask import Flask
import socket
import platform
import psutil



app = Flask(__name__)

@app.route("/")
def home():
	hostname = socket.gethostname()
	sistema = platform.system()
	cpu = psutil.cpu_percent(interval=1)

	memoria = psutil.virtual_memory()
	ram_percent = memoria.percent
	ram_total = memoria.total / (1024**3)
	ram_usada = memoria.used / (1024**3)



	return f"""
	<h1>Infra Status</h1>
	<p>Aplicacao iniciada com sucesso!</p>
	<p><strong>Hostname:</strong> {hostname}</P>
	<p><strong>Sistema operacional:</strong> {sistema}</p>
	<p><strong>Uso da CPU:</strong> {cpu}%</p>
	<p><strong>Uso da RAM:</strong> {ram_percent}%</p>
	<p><strong>RAM total:</strong> {ram_total:.2f} GiB</p>
	<p><strong>RAM utilizada:</strong> {ram_usada:.2f} GiB</p>

	"""

@app.route ("/api/metrics")
def metrics():
	memoria = psutil.virtual_memory()

	dados = {
		"hostname": socket.gethostname(),
		"sistema": platform.system(),
		"cpu_percent": psutil.cpu_percent(interval=1),
		"ram_percent": memoria.percent,
		"ram_total_gib": round (memoria.total / (1024**3),2),
		"ram_used_gib": round(memoria.used / (1024**3), 2),

}
	return dados

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=False)

