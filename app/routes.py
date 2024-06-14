from flask import Blueprint, jsonify
from .services import get_cpu_usage, get_memory_usage, get_disk_usage, get_network_usage, get_virtual_memory_usage

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def home():
    return 'Hello, World!'

@main_bp.route('/monitor/cpu', methods=['GET'])
def cpu_usage():
    return jsonify(get_cpu_usage())

@main_bp.route('/monitor/memory', methods=['GET'])
def memory_usage():
    return jsonify(get_memory_usage())

@main_bp.route('/monitor/disk', methods=['GET'])
def disk_usage():
    return jsonify(get_disk_usage())
    
@main_bp.route('/monitor/network', methods=['GET'])
def network_usage():
    return jsonify(get_network_usage())

@main_bp.route('/monitor/virtual_memory', methods=['GET'])
def virtual_memory_usage():
    return jsonify(get_virtual_memory_usage())
    

@main_bp.route('/monitor', methods=['GET'])
def get_monitor_data():
    data = {
        'cpuUsage': get_cpu_usage(),
        'memoryUsage': get_memory_usage(),
        'diskUsage': get_disk_usage(),
        'networkUsage': get_network_usage(),
        'virtualMemoryUsage': get_virtual_memory_usage()
    }
    return jsonify(data)