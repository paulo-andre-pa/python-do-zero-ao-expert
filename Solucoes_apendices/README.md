# Python do Zero ao Expert — código do livro

Código de todos os exemplos, trabalhos práticos e projetos do livro *Python do Zero ao Expert*, de Paulo Muhongo (Paulo Muhongo Editorial).

## Como usar

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python capitulo_02_variaveis_tipos_e_operadores/executar_todos.py
```

Os exemplos de cada capítulo estão numerados pela ordem em que aparecem no livro; alguns dependem de definições dos exemplos anteriores do mesmo capítulo — por isso cada pasta tem um `executar_todos.py`, que os executa por ordem. Os exemplos que pedem dados esperam pela sua resposta. Os projetos têm a sua própria estrutura (`src/` e `tests/`): entre na pasta do projeto e execute `python -m pytest`.

## Conteúdo

- **Capítulo 1** — Primeiros passos com Python: [`capitulo_01_primeiros_passos_com_python/`](capitulo_01_primeiros_passos_com_python/)
- **Capítulo 2** — Variáveis, tipos e operadores: [`capitulo_02_variaveis_tipos_e_operadores/`](capitulo_02_variaveis_tipos_e_operadores/)
- **Capítulo 3** — Texto: trabalhar com strings: [`capitulo_03_texto_trabalhar_com_strings/`](capitulo_03_texto_trabalhar_com_strings/)
- **Capítulo 4** — Decisões: if, elif, else e match: [`capitulo_04_decisoes_if_elif_else_e_match/`](capitulo_04_decisoes_if_elif_else_e_match/)
- **Capítulo 5** — Ciclos: while e for: [`capitulo_05_ciclos_while_e_for/`](capitulo_05_ciclos_while_e_for/)
- **Capítulo 6** — Listas e tuplos: [`capitulo_06_listas_e_tuplos/`](capitulo_06_listas_e_tuplos/)
- **Capítulo 7** — Dicionários e conjuntos: [`capitulo_07_dicionarios_e_conjuntos/`](capitulo_07_dicionarios_e_conjuntos/)
- **Capítulo 8** — Funções: [`capitulo_08_funcoes/`](capitulo_08_funcoes/)
- **Capítulo 9** — Ficheiros e exceções: [`capitulo_09_ficheiros_e_excecoes/`](capitulo_09_ficheiros_e_excecoes/)
- **Capítulo 10** — Módulos, pacotes e ambientes virtuais: [`capitulo_10_modulos_pacotes_e_ambientes_virtuais/`](capitulo_10_modulos_pacotes_e_ambientes_virtuais/)
- **Capítulo 11** — Programação orientada a objetos: [`capitulo_11_programacao_orientada_a_objetos/`](capitulo_11_programacao_orientada_a_objetos/)
- **Capítulo 12** — POO avançada: herança, dataclasses e métodos especiais: [`capitulo_12_poo_avancada_heranca_dataclasses_e_metod/`](capitulo_12_poo_avancada_heranca_dataclasses_e_metod/)
- **Capítulo 13** — Iteradores, geradores e compreensões: [`capitulo_13_iteradores_geradores_e_compreensoes/`](capitulo_13_iteradores_geradores_e_compreensoes/)
- **Capítulo 14** — Programação funcional e decoradores: [`capitulo_14_programacao_funcional_e_decoradores/`](capitulo_14_programacao_funcional_e_decoradores/)
- **Capítulo 15** — Testes automatizados com pytest: [`capitulo_15_testes_automatizados_com_pytest/`](capitulo_15_testes_automatizados_com_pytest/)
- **Capítulo 16** — Dados persistentes: CSV, JSON e SQLite: [`capitulo_16_dados_persistentes_csv_json_e_sqlite/`](capitulo_16_dados_persistentes_csv_json_e_sqlite/)
- **Capítulo 17** — Expressões regulares, datas e outras ferramentas essenciais: [`capitulo_17_expressoes_regulares_datas_e_outras_ferr/`](capitulo_17_expressoes_regulares_datas_e_outras_ferr/)
- **Capítulo 18** — Tipagem estática e mypy: [`capitulo_18_tipagem_estatica_e_mypy/`](capitulo_18_tipagem_estatica_e_mypy/)
- **Capítulo 19** — Metaprogramação: gestores de contexto, descritores e metaclasses: [`capitulo_19_metaprogramacao_gestores_de_contexto_des/`](capitulo_19_metaprogramacao_gestores_de_contexto_des/)
- **Capítulo 20** — Concorrência: threads, processos e asyncio: [`capitulo_20_concorrencia_threads_processos_e_asyncio/`](capitulo_20_concorrencia_threads_processos_e_asyncio/)
- **Capítulo 21** — Algoritmos, estruturas de dados e desempenho: [`capitulo_21_algoritmos_estruturas_de_dados_e_desempe/`](capitulo_21_algoritmos_estruturas_de_dados_e_desempe/)
- **Capítulo 22** — Engenharia de software em Python: [`capitulo_22_engenharia_de_software_em_python/`](capitulo_22_engenharia_de_software_em_python/)
- **Capítulo 23** — Redes, HTTP e APIs web: [`capitulo_23_redes_http_e_apis_web/`](capitulo_23_redes_http_e_apis_web/)
- **Capítulo 24** — Análise de dados com NumPy, pandas e Matplotlib: [`capitulo_24_analise_de_dados_com_numpy_pandas_e_matp/`](capitulo_24_analise_de_dados_com_numpy_pandas_e_matp/)
- **Capítulo 25** — Python por dentro: objetos, memória e o modelo de dados: [`capitulo_25_python_por_dentro_objetos_memoria_e_o_mo/`](capitulo_25_python_por_dentro_objetos_memoria_e_o_mo/)
- **Capítulo 26** — Python idiomático: boas práticas e armadilhas: [`capitulo_26_python_idiomatico_boas_praticas_e_armadi/`](capitulo_26_python_idiomatico_boas_praticas_e_armadi/)
- **Capítulo 27** — Padrões de projeto e arquitetura: [`capitulo_27_padroes_de_projeto_e_arquitetura/`](capitulo_27_padroes_de_projeto_e_arquitetura/)
- **Capítulo 28** — Aprendizagem automática com scikit-learn: [`capitulo_28_aprendizagem_automatica_com_scikit_learn/`](capitulo_28_aprendizagem_automatica_com_scikit_learn/)
- **Capítulo 29** — Aplicações web com Flask: [`capitulo_29_aplicacoes_web_com_flask/`](capitulo_29_aplicacoes_web_com_flask/)
- **Projeto 1** — Gestor de tarefas de linha de comandos: [`projeto_1_gestor_de_tarefas_de_linha_de_comandos/`](projeto_1_gestor_de_tarefas_de_linha_de_comandos/)
- **Projeto 2** — Sistema de gestão de biblioteca: [`projeto_2_sistema_de_gestao_de_biblioteca/`](projeto_2_sistema_de_gestao_de_biblioteca/)
- **Projeto 3** — Painel de análise de vendas: [`projeto_3_painel_de_analise_de_vendas/`](projeto_3_painel_de_analise_de_vendas/)
- **Projeto 4** — API REST de reserva de salas: [`projeto_4_api_rest_de_reserva_de_salas/`](projeto_4_api_rest_de_reserva_de_salas/)
- **Projeto 5** — Monitor de serviços assíncrono: [`projeto_5_monitor_de_servicos_assincrono/`](projeto_5_monitor_de_servicos_assincrono/)
- **Projeto 6** — Triagem inteligente de pedidos de suporte: [`projeto_6_triagem_inteligente_de_pedidos_de_suport/`](projeto_6_triagem_inteligente_de_pedidos_de_suport/)
- **Apêndice A** — Guia de referência rápida: [`apendice_A_guia_de_referencia_rapida/`](apendice_A_guia_de_referencia_rapida/)
- **Apêndice B** — Soluções de exercícios selecionados: [`apendice_B_solucoes_de_exercicios_selecionados/`](apendice_B_solucoes_de_exercicios_selecionados/)
- **Apêndice C** — Preparação para entrevistas técnicas: [`apendice_C_preparacao_para_entrevistas_tecnicas/`](apendice_C_preparacao_para_entrevistas_tecnicas/)

Todos os exemplos foram testados com Python 3.13.
