from main_analyze_results import compare_json_files
import json


def test_missing_matches(tmp_path):
    expected = tmp_path / "main_gt.json"
    expected.write_text("""\
[
    {
        "file": "main.py",
        "line_number": 3,
        "col_offset": 5,
        "function": "param_func",
        "type": [
            "str"
        ]
    },
    {
        "file": "main.py",
        "line_number": 7,
        "col_offset": 5,
        "function": "func",
        "type": [
            "str"
        ]
    },
    {
        "file": "main.py",
        "line_number": 7,
        "col_offset": 10,
        "function": "func",
        "parameter": "a",
        "type": [
            "callable"
        ]
    },
    {
        "file": "main.py",
        "line_number": 11,
        "col_offset": 1,
        "variable": "b",
        "type": [
            "str"
        ]
    }
]
    """)

    output = tmp_path / "main_results.json"
    output.write_text("""\
[
    {
        "file": "main.py",
        "line_number": 3,
        "col_offset": 5,
        "function": "param_func",
        "type": [
            "str"
        ]
    },
    {
        "file": "main.py",
        "line_number": 7,
        "col_offset": 10,
        "function": "func",
        "parameter": "a",
        "type": [
            "callable"
        ]
    },
    {
        "file": "main.py",
        "line_number": 7,
        "col_offset": 5,
        "function": "func",
        "type": [
            "str"
        ]
    }
]
    """)

    results = compare_json_files(expected, output)
    print(results)

    assert len(results['missing_matches']) == 1
    assert results['missing_matches'] == [json.loads("""
        {
            "file": "main.py",
            "line_number": 11,
            "col_offset": 1,
            "variable": "b",
            "type": [
                "str"
            ],
            "out_type": []
        }
    """)
    ]
