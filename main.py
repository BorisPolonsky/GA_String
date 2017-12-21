from ga_string import GaString
from argparse import ArgumentParser


def main(args):
    ga = GaString(args.predefined_char_set)
    community = []
    target = args.target_sequence
    prev_string = None
    ga.set_target(target)
    for i in range(args.max_iteration):
        while len(community) < args.max_community_size:
            community.append(ga.generate_individual(len(target)))
        community = ga.fixed_ratio_individual_selection(community, args.selection_ratio)
        community += ga.single_gene_mutation(community, args.mutation_prob, True)
        community = ga.sort_individual(community, True)
        community = community[:args.max_community_size]
        if prev_string != community[0]:
            prev_string = community[0]
            print(prev_string)
        if prev_string == target:
            break


#  Here goes the test
if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument("--predefined-char-set", action="store", type=str, default="Default", 
                            help='Could be either "Default", "Latin", "Number" or "Symbol". ')
    arg_parser.add_argument("--max-iteration", action="store", type=int, default=3000,  
                            help='Maximum number of iteration. ')
    arg_parser.add_argument("--max-community-size", action="store", type=int, default=40, 
                            help='Maximum number of individuals to keep at the same time. ')
    arg_parser.add_argument("--target-sequence", action="store", type=str, default="Too young, too simple, sometimes naive. ", 
                            help="Sequence to be generated through GA. ")
    arg_parser.add_argument("--selection-ratio", action="store", type=int, default=0.5,
                            help="Ratio configuration in selection. ")
    arg_parser.add_argument("--mutation-prob", action="store", type=int, default=0.5,
                            help="The probability for each character to mutate. ")
    args = arg_parser.parse_args()
    main(args)
