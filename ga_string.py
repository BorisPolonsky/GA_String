import random


class GaString:
    default_dict_set = {"Latin": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                        "Default": list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ~!@#$%^&*()_+`1234567890-={}|:\"<>?[]\\;',./"),
                        "Number": list("0123456789"),
                        "Symbol": " ~!@#$%^&*()_+`-={}|:\"<>?[]\\;',./"}

    def __init__(self, char_set="Default"):
        self.str_origin = ""
        self.str_target = ""
        self.Parents_Lst = []
        self.char_set = None
        self.set_char_set(char_set)

    def calculate_fitness_scores(self, origin_list, target):
        z = len(target)
        scores = []
        for individuals in origin_list:
            if z != len(individuals):
                scores.append(-1)
            else:
                matched_ch_num = 0
                for i in range(z):
                    if individuals[i] == target[i]:
                        matched_ch_num += 1
                scores.append(float(matched_ch_num)/float(z))
        return scores

    def set_target(self, target):
        if type(target) == str:
            self.str_target = target

    def set_char_set(self, dic_type):
        if type(dic_type) == list:
            self.char_set = dic_type[:]
        elif type(dic_type) == str:
            self.char_set = self.default_dict_set[dic_type]

    def get_char_set(self):
        return self.char_set

    def char_set_extend(self, additional_char_set):
        if type(additional_char_set) == str:
            if additional_char_set in self.default_dict_set.keys():
                self.char_set += self.default_dict_set[additional_char_set]
        elif type(additional_char_set) == list:
            self.char_set += additional_char_set

    def single_gene_mutation(self, individuals, mutation_rate, filter_non_mutant=False):
        mutants = []
        if type(mutation_rate)==float:
            for individual in individuals:
                if random.random() <= mutation_rate:
                    gene_individual = list(individual)
                    gene_individual[random.randint(0,len(gene_individual)-1)] = \
                        self.char_set[random.randint(0, len(self.char_set) - 1)]  # bug
                    mutants.append("".join(gene_individual))
                elif not filter_non_mutant:
                    mutants.append(individual)
        elif type(mutation_rate) == list:
            for individual, rate in zip(individuals, mutation_rate):
                if random.random() <= rate:
                    gene_individual = list(individual)
                    gene_individual[random.randint(0, len(gene_individual)-1)] = \
                        self.char_set[random.randint(0, len(self.char_set) - 1)]  # bug
                    mutants.append("".join(gene_individual))
                elif not filter_non_mutant:
                    mutants.append(individual)
        return mutants

    def pairwise_crossover(self, parent1, parent2):
        gene_p1 = list(parent1)
        gene_p2 = list(parent2)
        if len(gene_p1) != len(gene_p2):
            return parent1, parent2
        else:
            pos1 = random.randint(0, len(gene_p1)-1)
            pos2 = random.randint(0, len(gene_p1)-1)
            if pos1 > pos2:
                pos1, pos2 = pos2, pos1
            #  gene_p1[pos1:pos2],gene_p2[pos1:,pos2]=gene_p2[pos1:pos2],gene_p1[pos1:pos2]#Didn't know why it doesn't work...
            #  substitution code:
            temp = gene_p1[pos1:pos2]
            gene_p1[pos1:pos2] = gene_p2[pos1:pos2]
            gene_p2[pos1:pos2] = temp
            return "".join(gene_p1), "".join(gene_p2)

    def fixed_ratio_individual_selection(self, individual_source, ratio=0.5):
        selected_generation = individual_source[:]
        selected_generation = self.sort_individual(selected_generation, True)
        num_selected = min(int(len(selected_generation) * ratio), len(selected_generation))
        selected_generation = selected_generation[:num_selected]
        return selected_generation

    def roulette_individual_selection(self, individual_source):
        selected_generation = []
        fitness_scores = self.calculate_fitness_scores(individual_source, self.str_target)
        for i in range(len(individual_source)):
            if random.random() <= fitness_scores[i]:
                selected_generation.append(individual_source[i])
        return selected_generation

    def generate_individual(self, str_len):
        seq = []
        for i in range(str_len):
            seq.append(self.char_set[random.randint(0, len(self.char_set) - 1)])
        return "".join(seq)

    def sort_individual(self, individuals, reverse=False):
        fitness_scores = self.calculate_fitness_scores(individuals, self.str_target)
        str_score_structure_list = []
        for i in range(len(individuals)):
            str_score_structure_list.append([individuals[i], fitness_scores[i]])
        str_score_structure_list = sorted(str_score_structure_list, key=lambda x: x[1], reverse=reverse)
        sorted_individual_list = list(map(lambda x: x[0], str_score_structure_list))
        return sorted_individual_list
