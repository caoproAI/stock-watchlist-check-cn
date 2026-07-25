# 测试

运行结构与边界检查：

```powershell
py -3 tests/validate_contract.py
```

该测试验证：

- 必需文件是否存在；
- `SKILL.md` 是否包含关键安全边界；
- 测试案例是否不少于10个；
- `agents/openai.yaml` 是否包含显示名称、品牌色和默认提示；
- 是否残留模板 TODO 或乱码替换字符。

这不是收益效果测试，也不能证明 Skill 能预测市场。
