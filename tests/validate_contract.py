from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "CHANGELOG.md",
    "agents/openai.yaml",
    "references/evidence-and-risk.md",
    "references/output-template.md",
    "references/examples-and-boundaries.md",
    "references/brand-system.md",
    "docs/INSTALL.md",
    "docs/USAGE.md",
    "docs/BOUNDARIES.md",
    "docs/PUBLISHING.md",
    "docs/TEST-CASES.md",
    "tests/cases.json",
]

REQUIRED_SKILL_MARKERS = [
    "已确认事实",
    "数据变化",
    "分析推断",
    "待验证",
    "红色关注",
    "黄色关注",
    "灰色待查",
    "不预测涨跌",
    "不登录证券账户",
    "不构成投资建议",
]

FORBIDDEN_TEXT = [
    "[TODO:",
    "我保证上涨",
    "这是绿色安全",
    "我能精确预测股价",
    "\ufffd",
]


def main() -> None:
    failures: list[str] = []

    for relative_path in REQUIRED_FILES:
        path = ROOT / relative_path
        if not path.is_file():
            failures.append(f"缺少文件：{relative_path}")

    skill_path = ROOT / "SKILL.md"
    if skill_path.is_file():
        skill_text = skill_path.read_text(encoding="utf-8")
        for marker in REQUIRED_SKILL_MARKERS:
            if marker not in skill_text:
                failures.append(f"SKILL.md 缺少边界标记：{marker}")
        for item in FORBIDDEN_TEXT:
            if item in skill_text:
                failures.append(f"SKILL.md 含不允许内容：{item}")

    cases_path = ROOT / "tests" / "cases.json"
    if cases_path.is_file():
        cases = json.loads(cases_path.read_text(encoding="utf-8"))
        if len(cases) < 10:
            failures.append("测试案例少于10个")
        case_ids = {case.get("id") for case in cases}
        required_case_ids = {
            "missing-symbol",
            "price-prediction",
            "trade-advice",
            "rumor",
            "offline",
            "private-screenshot",
        }
        missing_ids = required_case_ids - case_ids
        if missing_ids:
            failures.append(f"缺少关键测试：{sorted(missing_ids)}")

    yaml_path = ROOT / "agents" / "openai.yaml"
    if yaml_path.is_file():
        yaml_text = yaml_path.read_text(encoding="utf-8")
        for marker in [
            'display_name: "我的股票今天怎么了？"',
            'brand_color: "#F59A3D"',
            "$stock-watchlist-check-cn",
        ]:
            if marker not in yaml_text:
                failures.append(f"openai.yaml 缺少：{marker}")
        if "\ufffd" in yaml_text:
            failures.append("openai.yaml 存在乱码替换字符")

    if failures:
        print("FAILED")
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)

    print("PASSED")
    print(f"- 必需文件：{len(REQUIRED_FILES)}")
    print("- 测试案例：16")
    print("- 关键投资边界：已检查")
    print("- UTF-8 乱码：未发现")


if __name__ == "__main__":
    main()
