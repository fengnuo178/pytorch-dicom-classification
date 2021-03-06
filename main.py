from model import *
import argparse

def main():
    parser = argparse.ArgumentParser(description="neural network framework for dicom datasets")

    parser.add_argument('--architecture', default='resnet152', type=str, help='a NN architecture supported by torchvision e.g. resnet152')
    parser.add_argument('--output_dim', default=8192, type=int, help='the final hidden layer\'s dim')
    parser.add_argument('--num_labels', default=2, type=int, help="# of labels")
    parser.add_argument('--k', default=5, type=int, help="\'k\'-fold")
    parser.add_argument('--src', type=str, help="all directories must be src-0, src-1, ..., src-k")
    parser.add_argument('--lr', default=1e-3, type=float, help="learning rate")
    parser.add_argument('--beta_1', default=0.9, type=float, help="first beta value")
    parser.add_argument('--beta_2', default=0.999, type=float, help="second beta value")
    parser.add_argument('--weight_decay', default=.0, type=float, help="weight decay")
    parser.add_argument('--nb_epochs', default=25, type=int, help="# of epochs")
    parser.add_argument('--batch_size', default=32, type=int, help="batch size")
    parser.add_argument('--start_fold', default=0, type=int, help="start fold")
    parser.add_argument('--end_fold', default=0, type=int, help="end fold, if it is 0, it will be interpreted as using full k fold")

    parser = parser.parse_args()

    architecture = parser.architecture
    output_dim = parser.output_dim
    num_labels = parser.num_labels
    k = parser.k
    src = [ parser.src + "-%d"%(i) for i in range(k) ]
    lr = parser.lr
    betas = (parser.beta_1, parser.beta_2)
    weight_decay = parser.weight_decay
    nb_epochs = parser.nb_epochs
    batch_size = parser.batch_size
    start_fold = parser.start_fold
    end_fold = parser.end_fold
    if end_fold == 0:
        end_fold = k
    if num_labels == 2:
        train(architecture, output_dim, k, src, binary_label, num_labels, lr, betas, weight_decay, nb_epochs, batch_size, start_fold, end_fold)
    else:
        train(architecture, output_dim, k, src, multi_label, num_labels, lr, betas, weight_decay, nb_epochs, batch_size, start_fold, end_fold)

if __name__ == "__main__":
    main()
