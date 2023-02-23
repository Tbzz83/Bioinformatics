library(tidyverse)
library(readxl)
library(ggplot2)

rarefaction <- read.delim('final.opti_mcc.groups.ave-std.summary')

rarefaction$group_num <- as.numeric(sub('F3D', '', rarefaction$group))

rarefaction <- rarefaction[order(rarefaction$group_num),]

# resetting row indices
row.names(rarefaction) <- 1:nrow(rarefaction)

# Scatter plot of invsimpson 
ggplot(subset(rarefaction, method == "ave"), aes(y=invsimpson, x=group)) +
  geom_point()

# combining samples based on time into early or late (so we have replicates)
rarefaction$category <- ifelse(rarefaction$group_num <=9, 'early', 'late')

# use a box plot to compare early and late invsimpson diversity
ggplot(subset(rarefaction, method == "ave"), aes(y=invsimpson, x=category)) +
  geom_boxplot()

# Creating variables to do a paired t-test BUT because of sample data they are different lengths so we can't
x <- rarefaction[rarefaction$category == 'early' & rarefaction$method == 'ave', 'invsimpson']
y <- rarefaction[rarefaction$category == 'late' & rarefaction$method == 'ave', 'invsimpson']


# Now to plot relative abundance of early vs late
otu_data <- read_tsv('final.opti_mcc.shared')%>%
  select(Group, starts_with('Otu'))%>%
  rename(sample_id = Group)%>%
  pivot_longer(-sample_id, names_to = 'otu', values_to = 'count')
  




taxonomy <- read_tsv('final.opti_mcc.0.03.cons.taxonomy')%>%
  select(OTU, Taxonomy)%>%
  rename_all(tolower) %>%
  mutate(taxonomy = str_replace_all(taxonomy, '\\(\\d+\\)', ''),
         taxonomy = str_replace(taxonomy, ';$', ''),
         taxonomy = str_replace_all(taxonomy, '"', ''))%>%
  separate(taxonomy, into = c('kingdom', 'phylum', 'class', 'order', 'family', 'genus'), sep = ';')


otu_rel_abund <- inner_join(otu_data, taxonomy, by='otu')%>%
  mutate(sample_num = substr(sample_id, 4, nchar(sample_id)))%>%
  mutate(status = ifelse(as.numeric(sample_num) > 9, 'late', 'early'))%>%
  select(-sample_num)%>%
  group_by(sample_id)%>%
  mutate(rel_abund = count/sum(count))%>%
  ungroup()%>%
  select(-count) %>%
  pivot_longer(cols = c('kingdom', 'phylum', 'class', 'order', 'family', 'genus', 'otu'), names_to = 'level', values_to ='taxon')

## Write below in terminal to check rel_abund does indeed add up to 1
# otu_rel_abund %>%
  # group_by(sample_id) %>%
  # summarize(total = sum(rel_abund))

otu_rel_abund %>%
  filter(level == 'phylum')%>%
  group_by(sample_id, status, taxon)%>%
  summarize(rel_abund = sum(rel_abund), .groups = 'drop')%>%
  group_by(status, taxon)%>%
  summarize(mean_rel_abund = mean(rel_abund)*100, .groups = 'drop')%>%
  ggplot(aes(x = status, y = mean_rel_abund, fill = taxon)) + geom_col() +
  theme_classic()
  

ggsave('Before_after_stacked_bar.tiff', width = 5, height = 4)
  



