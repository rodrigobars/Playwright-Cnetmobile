from pprint import pprint

json1 = [
    {
        "numero": 1,
        "tipo": "S",
        "disputaPorValorUnitario": True,
        "possuiOrcamentoSigiloso": False,
        "identificador": "1",
        "descricao": "Condimento",
        "criterioJulgamento": "1",
        "homologado": True,
        "situacaoEnvioResultado": "SP",
        "numeroSessaoJulgHab": 1,
        "tipoTratamentoDiferenciadoMeEpp": "1",
        "participacaoExclusivaMeEppOuEquiparadas": True,
        "situacao": "1",
        "fase": "AE",
        "quantidadeSolicitada": 93,
        "criterioValor": "E",
        "valorEstimadoUnitario": 19.5100,
        "valorEstimadoTotal": 1814.4300,
        "julgHabEncerrada": True,
        "propostaItem": {
            "quantidadeOfertada": 93,
            "marcaFabricante": "tempera bem ",
            "modeloVersao": "500 grs",
            "situacao": "2",
            "empatadoComoMelhorClassificado": False,
            "valores": {
                "valorPropostaInicial": {
                    "valorInformado": 19.5000,
                    "valorCalculado": {
                        "valorUnitario": 19.5000,
                        "valorTotal": 1813.5000
                    }
                },
                "valorPropostaInicialOuLances": {
                    "valorInformado": 19.5000,
                    "valorCalculado": {
                        "valorUnitario": 19.5000,
                        "valorTotal": 1813.5000
                    }
                }
            },
            "participante": {
                "identificacao": "31900031000122",
                "nome": "LENISA DISTRIBUIDORA LTDA",
                "tipo": "J"
            },
            "declaracaoMeEpp": True,
            "canalChatAberto": False
        }
    },
    {
        "numero": 2,
        "tipo": "S",
        "disputaPorValorUnitario": True,
        "possuiOrcamentoSigiloso": False,
        "identificador": "2",
        "descricao": "Condimento",
        "criterioJulgamento": "1",
        "homologado": True,
        "situacaoEnvioResultado": "SP",
        "numeroSessaoJulgHab": 1,
        "tipoTratamentoDiferenciadoMeEpp": "1",
        "participacaoExclusivaMeEppOuEquiparadas": True,
        "situacao": "1",
        "fase": "AE",
        "quantidadeSolicitada": 70,
        "criterioValor": "E",
        "valorEstimadoUnitario": 18.8500,
        "valorEstimadoTotal": 1319.5000,
        "julgHabEncerrada": True,
        "propostaItem": {
            "quantidadeOfertada": 70,
            "marcaFabricante": "tempera bem",
            "modeloVersao": "500 grs",
            "situacao": "2",
            "empatadoComoMelhorClassificado": False,
            "valores": {
                "valorPropostaInicial": {
                    "valorInformado": 18.8400,
                    "valorCalculado": {
                        "valorUnitario": 18.8400,
                        "valorTotal": 1318.8000
                    }
                },
                "valorPropostaInicialOuLances": {
                    "valorInformado": 10.0000,
                    "valorCalculado": {
                        "valorUnitario": 10.0000,
                        "valorTotal": 700.0000
                    }
                }
            },
            "participante": {
                "identificacao": "31900031000122",
                "nome": "LENISA DISTRIBUIDORA LTDA",
                "tipo": "J"
            },
            "declaracaoMeEpp": True,
            "canalChatAberto": False
        }
    },
    {
        "numero": 3,
        "tipo": "S",
        "disputaPorValorUnitario": True,
        "possuiOrcamentoSigiloso": False,
        "identificador": "3",
        "descricao": "Condimento",
        "criterioJulgamento": "1",
        "homologado": True,
        "situacaoEnvioResultado": "SP",
        "numeroSessaoJulgHab": 1,
        "tipoTratamentoDiferenciadoMeEpp": "1",
        "participacaoExclusivaMeEppOuEquiparadas": True,
        "situacao": "1",
        "fase": "AE",
        "quantidadeSolicitada": 58,
        "criterioValor": "E",
        "valorEstimadoUnitario": 9.9900,
        "valorEstimadoTotal": 579.4200,
        "julgHabEncerrada": True,
        "propostaItem": {
            "quantidadeOfertada": 58,
            "marcaFabricante": "chinesinho",
            "modeloVersao": "30grs",
            "situacao": "2",
            "empatadoComoMelhorClassificado": False,
            "valores": {
                "valorPropostaInicial": {
                    "valorInformado": 9.9800,
                    "valorCalculado": {
                        "valorUnitario": 9.9800,
                        "valorTotal": 578.8400
                    }
                },
                "valorPropostaInicialOuLances": {
                    "valorInformado": 5.0000,
                    "valorCalculado": {
                        "valorUnitario": 5.0000,
                        "valorTotal": 290.0000
                    }
                }
            },
            "participante": {
                "identificacao": "31900031000122",
                "nome": "LENISA DISTRIBUIDORA LTDA",
                "tipo": "J"
            },
            "declaracaoMeEpp": True,
            "canalChatAberto": False
        }
    },
    {
        "numero": 4,
        "tipo": "S",
        "disputaPorValorUnitario": True,
        "possuiOrcamentoSigiloso": False,
        "identificador": "4",
        "descricao": "Condimento",
        "criterioJulgamento": "1",
        "homologado": True,
        "situacaoEnvioResultado": "SP",
        "numeroSessaoJulgHab": 1,
        "tipoTratamentoDiferenciadoMeEpp": "1",
        "participacaoExclusivaMeEppOuEquiparadas": True,
        "situacao": "1",
        "fase": "AE",
        "quantidadeSolicitada": 6,
        "criterioValor": "E",
        "valorEstimadoUnitario": 70.9600,
        "valorEstimadoTotal": 425.7600,
        "julgHabEncerrada": True,
        "propostaItem": {
            "quantidadeOfertada": 6,
            "marcaFabricante": "tempera bem ",
            "modeloVersao": "500 grs",
            "situacao": "2",
            "empatadoComoMelhorClassificado": False,
            "valores": {
                "valorPropostaInicial": {
                    "valorInformado": 70.9500,
                    "valorCalculado": {
                        "valorUnitario": 70.9500,
                        "valorTotal": 425.7000
                    }
                },
                "valorPropostaInicialOuLances": {
                    "valorInformado": 25.0000,
                    "valorCalculado": {
                        "valorUnitario": 25.0000,
                        "valorTotal": 150.0000
                    }
                }
            },
            "participante": {
                "identificacao": "31900031000122",
                "nome": "LENISA DISTRIBUIDORA LTDA",
                "tipo": "J"
            },
            "declaracaoMeEpp": True,
            "canalChatAberto": False
        }
    },
    {
        "numero": 5,
        "tipo": "S",
        "disputaPorValorUnitario": True,
        "possuiOrcamentoSigiloso": False,
        "identificador": "5",
        "descricao": "Tempero",
        "criterioJulgamento": "1",
        "homologado": True,
        "situacaoEnvioResultado": "SP",
        "numeroSessaoJulgHab": 1,
        "tipoTratamentoDiferenciadoMeEpp": "1",
        "participacaoExclusivaMeEppOuEquiparadas": True,
        "situacao": "1",
        "fase": "AE",
        "quantidadeSolicitada": 144,
        "criterioValor": "E",
        "valorEstimadoUnitario": 21.5200,
        "valorEstimadoTotal": 3098.8800,
        "julgHabEncerrada": True,
        "propostaItem": {
            "quantidadeOfertada": 144,
            "marcaFabricante": "tempera bem",
            "modeloVersao": "500 grs",
            "situacao": "2",
            "empatadoComoMelhorClassificado": False,
            "valores": {
                "valorPropostaInicial": {
                    "valorInformado": 21.5100,
                    "valorCalculado": {
                        "valorUnitario": 21.5100,
                        "valorTotal": 3097.4400
                    }
                },
                "valorPropostaInicialOuLances": {
                    "valorInformado": 19.0000,
                    "valorCalculado": {
                        "valorUnitario": 19.0000,
                        "valorTotal": 2736.0000
                    }
                }
            },
            "participante": {
                "identificacao": "31900031000122",
                "nome": "LENISA DISTRIBUIDORA LTDA",
                "tipo": "J"
            },
            "declaracaoMeEpp": True,
            "canalChatAberto": False
        }
    },
    {
        "numero": 6,
        "tipo": "S",
        "disputaPorValorUnitario": True,
        "possuiOrcamentoSigiloso": False,
        "identificador": "6",
        "descricao": "Condimento",
        "criterioJulgamento": "1",
        "homologado": True,
        "situacaoEnvioResultado": "SP",
        "numeroSessaoJulgHab": 1,
        "tipoTratamentoDiferenciadoMeEpp": "1",
        "participacaoExclusivaMeEppOuEquiparadas": True,
        "situacao": "1",
        "fase": "AE",
        "quantidadeSolicitada": 600,
        "criterioValor": "E",
        "valorEstimadoUnitario": 15.9300,
        "valorEstimadoTotal": 9558.0000,
        "julgHabEncerrada": True,
        "propostaItem": {
            "quantidadeOfertada": 600,
            "marcaFabricante": "tempero bem",
            "modeloVersao": "kg",
            "situacao": "2",
            "empatadoComoMelhorClassificado": False,
            "valores": {
                "valorPropostaInicial": {
                    "valorInformado": 15.9200,
                    "valorCalculado": {
                        "valorUnitario": 15.9200,
                        "valorTotal": 9552.0000
                    }
                },
                "valorPropostaInicialOuLances": {
                    "valorInformado": 10.0000,
                    "valorCalculado": {
                        "valorUnitario": 10.0000,
                        "valorTotal": 6000.0000
                    }
                }
            },
            "participante": {
                "identificacao": "31900031000122",
                "nome": "LENISA DISTRIBUIDORA LTDA",
                "tipo": "J"
            },
            "declaracaoMeEpp": True,
            "canalChatAberto": False
        }
    },
    {
        "numero": 7,
        "tipo": "S",
        "disputaPorValorUnitario": True,
        "possuiOrcamentoSigiloso": False,
        "identificador": "7",
        "descricao": "Condimento",
        "criterioJulgamento": "1",
        "homologado": True,
        "situacaoEnvioResultado": "SP",
        "numeroSessaoJulgHab": 1,
        "tipoTratamentoDiferenciadoMeEpp": "1",
        "participacaoExclusivaMeEppOuEquiparadas": True,
        "situacao": "1",
        "fase": "AE",
        "quantidadeSolicitada": 33,
        "criterioValor": "E",
        "valorEstimadoUnitario": 13.7000,
        "valorEstimadoTotal": 452.1000,
        "julgHabEncerrada": True,
        "propostaItem": {
            "quantidadeOfertada": 33,
            "marcaFabricante": "tempera bem",
            "modeloVersao": "500 grs",
            "situacao": "2",
            "empatadoComoMelhorClassificado": False,
            "valores": {
                "valorPropostaInicial": {
                    "valorInformado": 13.6900,
                    "valorCalculado": {
                        "valorUnitario": 13.6900,
                        "valorTotal": 451.7700
                    }
                },
                "valorPropostaInicialOuLances": {
                    "valorInformado": 9.0000,
                    "valorCalculado": {
                        "valorUnitario": 9.0000,
                        "valorTotal": 297.0000
                    }
                }
            },
            "participante": {
                "identificacao": "31900031000122",
                "nome": "LENISA DISTRIBUIDORA LTDA",
                "tipo": "J"
            },
            "declaracaoMeEpp": True,
            "canalChatAberto": False
        }
    },
    {
        "numero": 8,
        "tipo": "S",
        "disputaPorValorUnitario": True,
        "possuiOrcamentoSigiloso": False,
        "identificador": "8",
        "descricao": "Condimento",
        "criterioJulgamento": "1",
        "homologado": True,
        "situacaoEnvioResultado": "SP",
        "numeroSessaoJulgHab": 1,
        "tipoTratamentoDiferenciadoMeEpp": "1",
        "participacaoExclusivaMeEppOuEquiparadas": True,
        "situacao": "1",
        "fase": "AE",
        "quantidadeSolicitada": 17,
        "criterioValor": "E",
        "valorEstimadoUnitario": 57.4800,
        "valorEstimadoTotal": 977.1600,
        "julgHabEncerrada": True,
        "propostaItem": {
            "quantidadeOfertada": 17,
            "marcaFabricante": "tempera bem",
            "modeloVersao": "500 g",
            "situacao": "2",
            "empatadoComoMelhorClassificado": False,
            "valores": {
                "valorPropostaInicial": {
                    "valorInformado": 57.4700,
                    "valorCalculado": {
                        "valorUnitario": 57.4700,
                        "valorTotal": 976.9900
                    }
                },
                "valorPropostaInicialOuLances": {
                    "valorInformado": 57.4700,
                    "valorCalculado": {
                        "valorUnitario": 57.4700,
                        "valorTotal": 976.9900
                    }
                }
            },
            "participante": {
                "identificacao": "31900031000122",
                "nome": "LENISA DISTRIBUIDORA LTDA",
                "tipo": "J"
            },
            "declaracaoMeEpp": True,
            "canalChatAberto": False
        }
    },
    {
        "numero": 9,
        "tipo": "S",
        "disputaPorValorUnitario": True,
        "possuiOrcamentoSigiloso": False,
        "identificador": "9",
        "descricao": "Condimento",
        "criterioJulgamento": "1",
        "homologado": True,
        "situacaoEnvioResultado": "SP",
        "numeroSessaoJulgHab": 1,
        "tipoTratamentoDiferenciadoMeEpp": "1",
        "participacaoExclusivaMeEppOuEquiparadas": True,
        "situacao": "1",
        "fase": "AE",
        "quantidadeSolicitada": 44,
        "criterioValor": "E",
        "valorEstimadoUnitario": 14.7000,
        "valorEstimadoTotal": 646.8000,
        "julgHabEncerrada": True,
        "propostaItem": {
            "quantidadeOfertada": 44,
            "marcaFabricante": "tempera bem",
            "modeloVersao": "500g",
            "situacao": "2",
            "empatadoComoMelhorClassificado": False,
            "valores": {
                "valorPropostaInicial": {
                    "valorInformado": 14.6900,
                    "valorCalculado": {
                        "valorUnitario": 14.6900,
                        "valorTotal": 646.3600
                    }
                },
                "valorPropostaInicialOuLances": {
                    "valorInformado": 6.0000,
                    "valorCalculado": {
                        "valorUnitario": 6.0000,
                        "valorTotal": 264.0000
                    }
                }
            },
            "participante": {
                "identificacao": "31900031000122",
                "nome": "LENISA DISTRIBUIDORA LTDA",
                "tipo": "J"
            },
            "declaracaoMeEpp": True,
            "canalChatAberto": False
        }
    },
    {
        "numero": 10,
        "tipo": "S",
        "disputaPorValorUnitario": True,
        "possuiOrcamentoSigiloso": False,
        "identificador": "10",
        "descricao": "Condimento",
        "criterioJulgamento": "1",
        "homologado": True,
        "situacaoEnvioResultado": "SP",
        "numeroSessaoJulgHab": 1,
        "tipoTratamentoDiferenciadoMeEpp": "1",
        "participacaoExclusivaMeEppOuEquiparadas": True,
        "situacao": "1",
        "fase": "AE",
        "quantidadeSolicitada": 23,
        "criterioValor": "E",
        "valorEstimadoUnitario": 12.3500,
        "valorEstimadoTotal": 284.0500,
        "julgHabEncerrada": True,
        "propostaItem": {
            "quantidadeOfertada": 23,
            "marcaFabricante": "tempera bem",
            "modeloVersao": "500g",
            "situacao": "2",
            "empatadoComoMelhorClassificado": False,
            "valores": {
                "valorPropostaInicial": {
                    "valorInformado": 12.3400,
                    "valorCalculado": {
                        "valorUnitario": 12.3400,
                        "valorTotal": 283.8200
                    }
                },
                "valorPropostaInicialOuLances": {
                    "valorInformado": 7.0000,
                    "valorCalculado": {
                        "valorUnitario": 7.0000,
                        "valorTotal": 161.0000
                    }
                }
            },
            "participante": {
                "identificacao": "31900031000122",
                "nome": "LENISA DISTRIBUIDORA LTDA",
                "tipo": "J"
            },
            "declaracaoMeEpp": True,
            "canalChatAberto": False
        }
    }
]

json2 = [
    {
        "numero": 1,
        "tipo": "S",
        "disputaPorValorUnitario": True,
        "possuiOrcamentoSigiloso": False,
        "identificador": "1",
        "descricao": "Condimento",
        "criterioJulgamento": "1",
        "homologado": True,
        "situacaoEnvioResultado": "SP",
        "numeroSessaoJulgHab": 1,
        "tipoTratamentoDiferenciadoMeEpp": "1",
        "participacaoExclusivaMeEppOuEquiparadas": True,
        "situacao": "1",
        "fase": "AE",
        "quantidadeSolicitada": 93,
        "criterioValor": "E",
        "valorEstimadoUnitario": 19.5100,
        "valorEstimadoTotal": 1814.4300,
        "julgHabEncerrada": True,
        "propostaItem": {
            "quantidadeOfertada": 93,
            "marcaFabricante": "TEMPERABEM",
            "modeloVersao": "CARACTERISTICO",
            "situacao": "6",
            "empatadoComoMelhorClassificado": False,
            "valores": {
                "valorPropostaInicial": {
                    "valorInformado": 19.5100,
                    "valorCalculado": {
                        "valorUnitario": 19.5100,
                        "valorTotal": 1814.4300
                    }
                },
                "valorPropostaInicialOuLances": {
                    "valorInformado": 16.9400,
                    "valorCalculado": {
                        "valorUnitario": 16.9400,
                        "valorTotal": 1575.4200
                    }
                }
            },
            "participante": {
                "identificacao": "09031962000182",
                "nome": "C C S VALENTE COMERCIO DE GENEROS ALIMENTICIOS",
                "tipo": "J"
            },
            "declaracaoMeEpp": True,
            "canalChatAberto": False
        }
    },
    {
        "numero": 2,
        "tipo": "S",
        "disputaPorValorUnitario": True,
        "possuiOrcamentoSigiloso": False,
        "identificador": "2",
        "descricao": "Condimento",
        "criterioJulgamento": "1",
        "homologado": True,
        "situacaoEnvioResultado": "SP",
        "numeroSessaoJulgHab": 1,
        "tipoTratamentoDiferenciadoMeEpp": "1",
        "participacaoExclusivaMeEppOuEquiparadas": True,
        "situacao": "1",
        "fase": "AE",
        "quantidadeSolicitada": 70,
        "criterioValor": "E",
        "valorEstimadoUnitario": 18.8500,
        "valorEstimadoTotal": 1319.5000,
        "julgHabEncerrada": True,
        "propostaItem": {
            "quantidadeOfertada": 70,
            "marcaFabricante": "TEMPERABEM",
            "modeloVersao": "CARACTERISTICO",
            "situacao": "6",
            "empatadoComoMelhorClassificado": False,
            "valores": {
                "valorPropostaInicial": {
                    "valorInformado": 18.8500,
                    "valorCalculado": {
                        "valorUnitario": 18.8500,
                        "valorTotal": 1319.5000
                    }
                },
                "valorPropostaInicialOuLances": {
                    "valorInformado": 11.4000,
                    "valorCalculado": {
                        "valorUnitario": 11.4000,
                        "valorTotal": 798.0000
                    }
                }
            },
            "participante": {
                "identificacao": "09031962000182",
                "nome": "C C S VALENTE COMERCIO DE GENEROS ALIMENTICIOS",
                "tipo": "J"
            },
            "declaracaoMeEpp": True,
            "canalChatAberto": False
        }
    },
    {
        "numero": 3,
        "tipo": "S",
        "disputaPorValorUnitario": True,
        "possuiOrcamentoSigiloso": False,
        "identificador": "3",
        "descricao": "Condimento",
        "criterioJulgamento": "1",
        "homologado": True,
        "situacaoEnvioResultado": "SP",
        "numeroSessaoJulgHab": 1,
        "tipoTratamentoDiferenciadoMeEpp": "1",
        "participacaoExclusivaMeEppOuEquiparadas": True,
        "situacao": "1",
        "fase": "AE",
        "quantidadeSolicitada": 58,
        "criterioValor": "E",
        "valorEstimadoUnitario": 9.9900,
        "valorEstimadoTotal": 579.4200,
        "julgHabEncerrada": True,
        "propostaItem": {
            "quantidadeOfertada": 58,
            "marcaFabricante": "KITANO/ZANA",
            "modeloVersao": "CARACTERISTICO",
            "situacao": "6",
            "empatadoComoMelhorClassificado": False,
            "valores": {
                "valorPropostaInicial": {
                    "valorInformado": 9.9900,
                    "valorCalculado": {
                        "valorUnitario": 9.9900,
                        "valorTotal": 579.4200
                    }
                },
                "valorPropostaInicialOuLances": {
                    "valorInformado": 4.0000,
                    "valorCalculado": {
                        "valorUnitario": 4.0000,
                        "valorTotal": 232.0000
                    }
                }
            },
            "participante": {
                "identificacao": "09031962000182",
                "nome": "C C S VALENTE COMERCIO DE GENEROS ALIMENTICIOS",
                "tipo": "J"
            },
            "declaracaoMeEpp": True,
            "canalChatAberto": False
        }
    },
    {
        "numero": 4,
        "tipo": "S",
        "disputaPorValorUnitario": True,
        "possuiOrcamentoSigiloso": False,
        "identificador": "4",
        "descricao": "Condimento",
        "criterioJulgamento": "1",
        "homologado": True,
        "situacaoEnvioResultado": "SP",
        "numeroSessaoJulgHab": 1,
        "tipoTratamentoDiferenciadoMeEpp": "1",
        "participacaoExclusivaMeEppOuEquiparadas": True,
        "situacao": "1",
        "fase": "AE",
        "quantidadeSolicitada": 6,
        "criterioValor": "E",
        "valorEstimadoUnitario": 70.9600,
        "valorEstimadoTotal": 425.7600,
        "julgHabEncerrada": True,
        "propostaItem": {
            "quantidadeOfertada": 6,
            "marcaFabricante": "TEMPERABEM",
            "modeloVersao": "CARACTERISTICO",
            "situacao": "6",
            "empatadoComoMelhorClassificado": False,
            "valores": {
                "valorPropostaInicial": {
                    "valorInformado": 70.9600,
                    "valorCalculado": {
                        "valorUnitario": 70.9600,
                        "valorTotal": 425.7600
                    }
                },
                "valorPropostaInicialOuLances": {
                    "valorInformado": 30.0000,
                    "valorCalculado": {
                        "valorUnitario": 30.0000,
                        "valorTotal": 180.0000
                    }
                }
            },
            "participante": {
                "identificacao": "09031962000182",
                "nome": "C C S VALENTE COMERCIO DE GENEROS ALIMENTICIOS",
                "tipo": "J"
            },
            "declaracaoMeEpp": True,
            "canalChatAberto": False
        }
    },
    {
        "numero": 5,
        "tipo": "S",
        "disputaPorValorUnitario": True,
        "possuiOrcamentoSigiloso": False,
        "identificador": "5",
        "descricao": "Tempero",
        "criterioJulgamento": "1",
        "homologado": True,
        "situacaoEnvioResultado": "SP",
        "numeroSessaoJulgHab": 1,
        "tipoTratamentoDiferenciadoMeEpp": "1",
        "participacaoExclusivaMeEppOuEquiparadas": True,
        "situacao": "1",
        "fase": "AE",
        "quantidadeSolicitada": 144,
        "criterioValor": "E",
        "valorEstimadoUnitario": 21.5200,
        "valorEstimadoTotal": 3098.8800,
        "julgHabEncerrada": True,
        "propostaItem": {
            "quantidadeOfertada": 144,
            "marcaFabricante": "TEMPERABEM",
            "modeloVersao": "CARACTERISTICO",
            "situacao": "6",
            "empatadoComoMelhorClassificado": False,
            "valores": {
                "valorPropostaInicial": {
                    "valorInformado": 21.5200,
                    "valorCalculado": {
                        "valorUnitario": 21.5200,
                        "valorTotal": 3098.8800
                    }
                },
                "valorPropostaInicialOuLances": {
                    "valorInformado": 21.0800,
                    "valorCalculado": {
                        "valorUnitario": 21.0800,
                        "valorTotal": 3035.5200
                    }
                }
            },
            "participante": {
                "identificacao": "09031962000182",
                "nome": "C C S VALENTE COMERCIO DE GENEROS ALIMENTICIOS",
                "tipo": "J"
            },
            "declaracaoMeEpp": True,
            "canalChatAberto": False
        }
    },
    {
        "numero": 6,
        "tipo": "S",
        "disputaPorValorUnitario": True,
        "possuiOrcamentoSigiloso": False,
        "identificador": "6",
        "descricao": "Condimento",
        "criterioJulgamento": "1",
        "homologado": True,
        "situacaoEnvioResultado": "SP",
        "numeroSessaoJulgHab": 1,
        "tipoTratamentoDiferenciadoMeEpp": "1",
        "participacaoExclusivaMeEppOuEquiparadas": True,
        "situacao": "1",
        "fase": "AE",
        "quantidadeSolicitada": 600,
        "criterioValor": "E",
        "valorEstimadoUnitario": 15.9300,
        "valorEstimadoTotal": 9558.0000,
        "julgHabEncerrada": True,
        "propostaItem": {
            "quantidadeOfertada": 600,
            "marcaFabricante": "TEMPERABEM/ZANA",
            "modeloVersao": "CARACTERISTICO",
            "situacao": "6",
            "empatadoComoMelhorClassificado": False,
            "valores": {
                "valorPropostaInicial": {
                    "valorInformado": 15.9300,
                    "valorCalculado": {
                        "valorUnitario": 15.9300,
                        "valorTotal": 9558.0000
                    }
                },
                "valorPropostaInicialOuLances": {
                    "valorInformado": 9.8000,
                    "valorCalculado": {
                        "valorUnitario": 9.8000,
                        "valorTotal": 5880.0000
                    }
                }
            },
            "participante": {
                "identificacao": "09031962000182",
                "nome": "C C S VALENTE COMERCIO DE GENEROS ALIMENTICIOS",
                "tipo": "J"
            },
            "declaracaoMeEpp": True,
            "canalChatAberto": False
        }
    },
    {
        "numero": 7,
        "tipo": "S",
        "disputaPorValorUnitario": True,
        "possuiOrcamentoSigiloso": False,
        "identificador": "7",
        "descricao": "Condimento",
        "criterioJulgamento": "1",
        "homologado": True,
        "situacaoEnvioResultado": "SP",
        "numeroSessaoJulgHab": 1,
        "tipoTratamentoDiferenciadoMeEpp": "1",
        "participacaoExclusivaMeEppOuEquiparadas": True,
        "situacao": "1",
        "fase": "AE",
        "quantidadeSolicitada": 33,
        "criterioValor": "E",
        "valorEstimadoUnitario": 13.7000,
        "valorEstimadoTotal": 452.1000,
        "julgHabEncerrada": True,
        "propostaItem": {
            "quantidadeOfertada": 33,
            "marcaFabricante": "TEMPERABEM/ZANA",
            "modeloVersao": "CARACTERISTICO",
            "situacao": "6",
            "empatadoComoMelhorClassificado": False,
            "valores": {
                "valorPropostaInicial": {
                    "valorInformado": 13.7000,
                    "valorCalculado": {
                        "valorUnitario": 13.7000,
                        "valorTotal": 452.1000
                    }
                },
                "valorPropostaInicialOuLances": {
                    "valorInformado": 9.9000,
                    "valorCalculado": {
                        "valorUnitario": 9.9000,
                        "valorTotal": 326.7000
                    }
                }
            },
            "participante": {
                "identificacao": "09031962000182",
                "nome": "C C S VALENTE COMERCIO DE GENEROS ALIMENTICIOS",
                "tipo": "J"
            },
            "declaracaoMeEpp": True,
            "canalChatAberto": False
        }
    },
    {
        "numero": 8,
        "tipo": "S",
        "disputaPorValorUnitario": True,
        "possuiOrcamentoSigiloso": False,
        "identificador": "8",
        "descricao": "Condimento",
        "criterioJulgamento": "1",
        "homologado": True,
        "situacaoEnvioResultado": "SP",
        "numeroSessaoJulgHab": 1,
        "tipoTratamentoDiferenciadoMeEpp": "1",
        "participacaoExclusivaMeEppOuEquiparadas": True,
        "situacao": "1",
        "fase": "AE",
        "quantidadeSolicitada": 17,
        "criterioValor": "E",
        "valorEstimadoUnitario": 57.4800,
        "valorEstimadoTotal": 977.1600,
        "julgHabEncerrada": True,
        "propostaItem": {
            "quantidadeOfertada": 17,
            "marcaFabricante": "TEMPERABEM/ZANA",
            "modeloVersao": "CARACTERISTICO",
            "situacao": "6",
            "empatadoComoMelhorClassificado": False,
            "valores": {
                "valorPropostaInicial": {
                    "valorInformado": 57.4800,
                    "valorCalculado": {
                        "valorUnitario": 57.4800,
                        "valorTotal": 977.1600
                    }
                },
                "valorPropostaInicialOuLances": {
                    "valorInformado": 57.4800,
                    "valorCalculado": {
                        "valorUnitario": 57.4800,
                        "valorTotal": 977.1600
                    }
                }
            },
            "participante": {
                "identificacao": "09031962000182",
                "nome": "C C S VALENTE COMERCIO DE GENEROS ALIMENTICIOS",
                "tipo": "J"
            },
            "declaracaoMeEpp": True,
            "canalChatAberto": False
        }
    },
    {
        "numero": 9,
        "tipo": "S",
        "disputaPorValorUnitario": True,
        "possuiOrcamentoSigiloso": False,
        "identificador": "9",
        "descricao": "Condimento",
        "criterioJulgamento": "1",
        "homologado": True,
        "situacaoEnvioResultado": "SP",
        "numeroSessaoJulgHab": 1,
        "tipoTratamentoDiferenciadoMeEpp": "1",
        "participacaoExclusivaMeEppOuEquiparadas": True,
        "situacao": "1",
        "fase": "AE",
        "quantidadeSolicitada": 44,
        "criterioValor": "E",
        "valorEstimadoUnitario": 14.7000,
        "valorEstimadoTotal": 646.8000,
        "julgHabEncerrada": True,
        "propostaItem": {
            "quantidadeOfertada": 44,
            "marcaFabricante": "TEMPERABEM/ZANA",
            "modeloVersao": "CARACTERISTICO",
            "situacao": "6",
            "empatadoComoMelhorClassificado": False,
            "valores": {
                "valorPropostaInicial": {
                    "valorInformado": 14.7000,
                    "valorCalculado": {
                        "valorUnitario": 14.7000,
                        "valorTotal": 646.8000
                    }
                },
                "valorPropostaInicialOuLances": {
                    "valorInformado": 13.3000,
                    "valorCalculado": {
                        "valorUnitario": 13.3000,
                        "valorTotal": 585.2000
                    }
                }
            },
            "participante": {
                "identificacao": "09031962000182",
                "nome": "C C S VALENTE COMERCIO DE GENEROS ALIMENTICIOS",
                "tipo": "J"
            },
            "declaracaoMeEpp": True,
            "canalChatAberto": False
        }
    },
    {
        "numero": 10,
        "tipo": "S",
        "disputaPorValorUnitario": True,
        "possuiOrcamentoSigiloso": False,
        "identificador": "10",
        "descricao": "Condimento",
        "criterioJulgamento": "1",
        "homologado": True,
        "situacaoEnvioResultado": "SP",
        "numeroSessaoJulgHab": 1,
        "tipoTratamentoDiferenciadoMeEpp": "1",
        "participacaoExclusivaMeEppOuEquiparadas": True,
        "situacao": "1",
        "fase": "AE",
        "quantidadeSolicitada": 23,
        "criterioValor": "E",
        "valorEstimadoUnitario": 12.3500,
        "valorEstimadoTotal": 284.0500,
        "julgHabEncerrada": True,
        "propostaItem": {
            "quantidadeOfertada": 23,
            "marcaFabricante": "TEMPERABEM/ZANA",
            "modeloVersao": "CARACTERISTICO",
            "situacao": "6",
            "empatadoComoMelhorClassificado": False,
            "valores": {
                "valorPropostaInicial": {
                    "valorInformado": 12.3500,
                    "valorCalculado": {
                        "valorUnitario": 12.3500,
                        "valorTotal": 284.0500
                    }
                },
                "valorPropostaInicialOuLances": {
                    "valorInformado": 8.6000,
                    "valorCalculado": {
                        "valorUnitario": 8.6000,
                        "valorTotal": 197.8000
                    }
                }
            },
            "participante": {
                "identificacao": "09031962000182",
                "nome": "C C S VALENTE COMERCIO DE GENEROS ALIMENTICIOS",
                "tipo": "J"
            },
            "declaracaoMeEpp": True,
            "canalChatAberto": False
        }
    }
]

first_json_groupItems = True

for dicionario in json1:
    if first_json_groupItems:
        dicionario.update( { 'propostaItem': [dicionario.pop('propostaItem')] } )
    else:
        dicionario['propostaItem'].append(dicionario.pop('propostaItem'))

pprint(json1)

# print(f'esqueleto: {skeleton} | objeto: {objeto}')

# skeleton.update( { 'objeto': objeto })

# print(f"\nfinal: {skeleton}")