class TestInput:
    test_dictionary_for_core_start =   {
    "devices": [
        {
            "id": "90",
            "listening": "false",
            "type": "PC",
            "name": "one",
            "ip": "10.0.0.1",
            "ip4_mask": "24",
            "mac": "00:00:00:00:00:01",
            "subnet": 0,
            "scanning": "false"
        },
        {
            "id": "10",
            "listening": "true",
            "type": "PC",
            "name": "two",
            "ip": "10.0.1.1",
            "mac": "00:00:00:00:00:02",
            "ip4_mask": "24",
            "subnet": 1,
            "scanning": "true",
            "username/pass": "root/pass",
            "scanner_binary": "/usr/bin/nmap",
            "arguments": "--ts -v -ip 10.0.0.1",
            "iterations": 1,
            "parallel_runs": 1,
            "end_condition": "on-scan-complete | time mm:ss"
        }],
    "networks": [
    ],

    "scenario_name": "scenarioA",
    "project_name": "projectA",
    "workspace_name": "workspaceA",
}