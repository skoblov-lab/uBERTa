import sys
from collections import namedtuple

VALID_CHROM = (*(f'chr{i}' for i in range(23)), 'chrX', 'chrY')
VALID_CHROM_FLANKS = {
    'chr1': (10000, 10000),
    'chr2': (10000, 10000),
    'chr3': (10000, 60000),
    'chr4': (10000, 10000),
    'chr5': (10000, 60000),
    'chr6': (60000, 60000),
    'chr7': (10000, 10000),
    'chr8': (60000, 60000),
    'chr9': (10000, 60000),
    'chr10': (10000, 10000),
    'chr11': (60000, 10000),
    'chr12': (10000, 10000),
    'chr13': (16000000, 10000),
    'chr14': (16000000, 160000),
    'chr15': (17000000, 10000),
    'chr16': (10000, 110000),
    'chr17': (60000, 10000),
    'chr18': (10000, 110000),
    'chr19': (60000, 10000),
    'chr20': (60000, 110000),
    'chr21': (5010000, 10000),
    'chr22': (10510000, 10000),
    'chrX': (10000, 10000),
    'chrY': (10000, 10000)
}

_columns = ['chrom', 'start', 'end', 'codon', 'strand', 'gene_id', 'group', 'level', 'analyzed', 'positive']
_defaults = [
    'Chrom', 'StartCodonStart', 'StartCodonEnd', 'StartCodonFetched',
    'Strand', 'GeneIDUnique', 'Group', 'LevelStartCodonStartFetchedAround2',
    'IsAnalyzed', 'IsPositive']

if sys.version < "3.7":
    ColNames = lambda: namedtuple('ColNames', _columns)(*_defaults)
else:
    ColNames = namedtuple('ColNames', _columns, defaults=_defaults)

ModelSetup = namedtuple('Setup', ['Config', 'Model', 'Tokenizer', 'ModelPath'])
RunSetup = namedtuple('Setup', ['BatchSize', 'Epochs', 'WarmupPerc'])
OptSetup = namedtuple('Setup', ['LearningRate', 'Epsilon', 'Betas', 'WeightDecay'])
StopSetup = namedtuple('Setup', ['Rounds', 'Tolerance'])

Scores = namedtuple('Scores', ['acc', 'roc_auc', 'f1', 'prec', 'rec'])


if __name__ == '__main__':
    raise RuntimeError()
