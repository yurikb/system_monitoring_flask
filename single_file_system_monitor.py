from flask import Flask, jsonify
import psutil

app = Flask(__name__)

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    return psutil.virtual_memory().percent

def get_disk_usage():
    return psutil.disk_usage('/').percent

def get_network_usage():
    return psutil.net_io_counters().bytes_sent

def get_virtual_memory_usage():
    return psutil.virtual_memory().percent

@app.route('/monitor/cpu', methods=['GET'])
def cpu_usage():
    return jsonify(get_cpu_usage())

@app.route('/monitor/memory', methods=['GET'])
def memory_usage():
    return jsonify(get_memory_usage())

@app.route('/monitor/disk', methods=['GET'])
def disk_usage():
    return jsonify(get_disk_usage())

@app.route('/', methods=['GET'])
def home():
    return 'Hello, World!'
    
@app.route('/monitor/network', methods=['GET'])
def network_usage():
    return jsonify(get_network_usage())

@app.route('/monitor/virtual_memory', methods=['GET'])
def virtual_memory_usage():
    return jsonify(get_virtual_memory_usage())
    

@app.route('/monitor', methods=['GET'])
def get_monitor_data():
    data = {
        'cpuUsage': get_cpu_usage(),
        'memoryUsage': get_memory_usage(),
        'diskUsage': get_disk_usage(),
        'networkUsage': get_network_usage(),
        'virtualMemoryUsage': get_virtual_memory_usage()
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)