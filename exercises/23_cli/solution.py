"""Exercise 23: CLI"""
import argparse

def create_training_parser():
    parser = argparse.ArgumentParser(description='Train a model')
    parser.add_argument('--model', type=str, required=True)
    parser.add_argument('--epochs', type=int, default=10)
    parser.add_argument('--lr', type=float, default=0.001)
    parser.add_argument('--verbose', action='store_true')
    return parser

def parse_training_args(args_list=None):
    parser = create_training_parser()
    return parser.parse_args(args_list)
