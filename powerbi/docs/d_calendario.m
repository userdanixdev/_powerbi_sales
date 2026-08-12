let
    MinData = #date(Date.Year(List.Min(f_vendas[Data da Venda])),1,1),
    MaxData = #date(Date.Year(List.Max(f_vendas[Data da Venda])),12,31),
    DifDias = Number.From(MaxData - MinData) + 1,
    Fonte = List.Dates(MinData, DifDias, #duration(1,0,0,0)),
    #"Convertido para Tabela" = Table.FromList(Fonte, Splitter.SplitByNothing(), null, null, ExtraValues.Error),
    #"Tipo Alterado" = Table.TransformColumnTypes(#"Convertido para Tabela",{{"Column1", type date}}),
    #"Colunas Renomeadas" = Table.RenameColumns(#"Tipo Alterado",{{"Column1", "Data"}}),
    #"Mês Inserido" = Table.AddColumn(#"Colunas Renomeadas", "Mês", each Date.Month([Data]), Int64.Type),
    #"Nome do Mês Inserido" = Table.AddColumn(#"Mês Inserido", "Nome do Mês", each Date.MonthName([Data]), type text),
    #"Colocar Cada Palavra Em Maiúscula" = Table.TransformColumns(#"Nome do Mês Inserido",{{"Nome do Mês", Text.Proper, type text}}),
    #"Ano Inserido" = Table.AddColumn(#"Colocar Cada Palavra Em Maiúscula", "Ano", each Date.Year([Data]), Int64.Type),
    #"Dia da Semana Inserido" = Table.AddColumn(#"Ano Inserido", "Dia da Semana", each Date.DayOfWeek([Data]), Int64.Type),
    #"Nome do Dia Inserido" = Table.AddColumn(#"Dia da Semana Inserido", "Nome do Dia", each Date.DayOfWeekName([Data]), type text),
    #"Colocar Cada Palavra Em Maiúscula1" = Table.TransformColumns(#"Nome do Dia Inserido",{{"Nome do Dia", Text.Proper, type text}})
in
    #"Colocar Cada Palavra Em Maiúscula1"