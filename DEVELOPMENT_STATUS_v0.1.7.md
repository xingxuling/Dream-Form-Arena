# Dream Form Arena｜Development Status v0.1.7-alpha.1

## 本轮北极星
让白蓝飞碟拥有真正能反转战场关系的核心机制，而不是只做“多功能弱辅助”。

## 已实现
- R 同调俘获：rise → wave → absorb → convert → release 五阶段状态机。
- 准星优先选择普通 Bot；无直接准星目标时使用前方视锥候选。
- 升空与施法期间降低机动，形成风险窗口。
- 吸入、隐藏、改写、释放的程序化视觉表现。
- 转化单位获得 12 秒 `ally` 阵营状态、蓝白标识、自动索敌与近战攻击。
- 原敌方 Bot 会在距离条件满足时转而攻击临时友军。
- 同调到期自动恢复敌对。
- 离开白蓝形态 / 目标失效时 fail-safe 回滚目标状态。
- 友军被玩家火箭、绿色冲撞、引力锚、扫描逻辑排除，避免默认友伤。
- Visual 外部 KayKit Bot 同步捕获高度、隐藏、友军朝向及蓝白 tint。

## 参数
- Brainwash cooldown: 14 s
- Ally duration: 12 s
- Capture cinematic: ~3.0 s
- Capturable: ordinary `bot` only

## 证据
- 四个 HTML 内联 JS 语法检查。
- 静态合同测试：五阶段状态机、R 上下文路由、友军 AI、敌我反击、回滚、Visual 同步。
- RCL 合同编译 + Native VM：PASS。Bytecode SHA-256: `b600a111c1ac31880710c2a99c22630632037ad90b7540db4d5d5296a666077f`。

## 风险 / 回滚
- 若同调过强：先缩短友军持续时间，再增大冷却，不删除机制。
- 若施法过慢：优先压缩 convert 阶段，不破坏五阶段表达。
- 若 Visual tint/动画异常：只回滚 Visual 投影层，Standalone 玩法权威不受影响。
