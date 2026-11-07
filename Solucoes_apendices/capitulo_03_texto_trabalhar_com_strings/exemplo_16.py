# Capítulo 3 — Texto: trabalhar com strings
# Secção: Unicode e codificação

senha = "Segura2026"
regras = {
    "8 ou mais carateres": len(senha) >= 8,
    "uma maiúscula": any(c.isupper() for c in senha),
    "uma minúscula": any(c.islower() for c in senha),
    "um algarismo": any(c.isdigit() for c in senha),
}
for regra, ok in regras.items():
    print(("✓" if ok else "✗"), regra)
print("Palavra-passe válida!" if all(regras.values()) else "Inválida.")
