library(tidyverse)
library(readxl)
library(ggtext)

metadata <- read_excel('raw_data/schubert.metadata.xlsx', na = "NA") %>%
  select(sample_id, disease_stat) %>%
  drop_na(disease_stat)
  


otu_counts <- read_tsv('raw_data/schubert.subsample.shared') %>%
  ## To drop label and numOtus columns
  # select(-label, -numOtus)
  select(Group, starts_with('Otu')) %>%
  rename(sample_id = Group) %>%
  pivot_longer(-sample_id, names_to = 'otu', values_to = 'count')


taxonomy <- read_tsv('raw_data/schubert.cons.taxonomy') %>%
  select(OTU, Taxonomy) %>%
  rename_all(tolower) %>%
  mutate(taxonomy = str_replace_all(taxonomy, '\\(\\d+\\)', ''),
         taxonomy = str_replace(taxonomy, ';$', '')) %>%
  separate(taxonomy, into = c('kingdom', 'phylum', 'class', 'order', 'family', 'genus'), sep = ';')

#metadata
#otu_counts
#taxonomy

otu_rel_abund <- inner_join(metadata, otu_counts, by='sample_id') %>%
  inner_join(., taxonomy, by='otu') %>%
  group_by(sample_id) %>%
  mutate(rel_abund = count/sum(count)) %>%
  ungroup() %>%
  select(-count) %>%
  pivot_longer(cols = c('kingdom', 'phylum', 'class', 'order', 'family', 'genus', 'otu'), names_to = 'level', values_to ='taxon') %>%
  mutate(disease_stat = factor(disease_stat, 
                               levels = c('NonDiarrhealControl', 'DiarrhealControl', 'Case'))) 
                        

otu_rel_abund %>%
  filter(level=='phylum') %>%
  group_by(disease_stat, sample_id, taxon) %>%
  summarize(rel_abund = sum(rel_abund), .groups = 'drop') %>%
  group_by(disease_stat, taxon) %>%
  summarize(mean_rel_abund = 100*mean(rel_abund), .groups = 'drop') %>%
  ggplot(aes(x = disease_stat, y = mean_rel_abund, fill = taxon)) + 
  geom_col()+
  scale_x_discrete(breaks=c('NonDiarrhealControl', 'DiarrhealControl', 'Case'),
                   labels=c('Healthy', 'Diarrhea, <br>*C. difficile*<br> negative', 'Diarrhea, <br>*C. difficile*<br> positive'))+
  labs(x=NULL, 
       y='Mean Relative Abundance (%)') + 
  theme_classic()+
  theme(axis.text.x=element_markdown())

ggsave('schubert_stacked_bar.tiff', width = 5, height = 4)
  
  
  
  
  
  
  
  