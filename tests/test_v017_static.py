from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
for name in ["Standalone","Debug","Lite","Visual"]:
    s=(root/f"Dream_Form_Arena_v0.1.7_{name}.html").read_text(encoding="utf-8")
    assert "function useBrainwash()" in s
    assert "phase:'rise'" in s and "c.phase='wave'" in s and "c.phase='absorb'" in s and "c.phase='convert'" in s and "c.phase='release'" in s
    assert "e.team='ally'" in s and "e.allyTime=12" in s
    assert "if(state.form.form===FORM.WHITEBLUE) useBrainwash()" in s
    assert "离开白蓝形态：同调俘获中断" in s
    assert "R 同调俘获" in s
    assert "version:'0.1.7-alpha.1'" in s
visual=(root/"Dream_Form_Arena_v0.1.7_Visual.html").read_text(encoding="utf-8")
assert "e.captureY||0" in visual and "new THREE.Color(0x65d7ff)" in visual
print("PASS: v0.1.7 brainwash static contracts")
