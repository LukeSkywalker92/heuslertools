from heuslertools.tem import TEMImage
import matplotlib.pyplot as plt
import argparse

def main():
    parser = argparse.ArgumentParser(description='Display .ser TEM images.')
    parser.add_argument('-f', '--files', nargs='+', type=str, help='File')
    parser.add_argument('-s', '--save', action='store_true', help='Save Images.')
    parser.add_argument('-e', '--extension', nargs='?', type=str, const='png', default='png')
    args = parser.parse_args()

    try:
        plt.style.use('heusler_plotting')
    except:
        pass

    for file in args.files:
        img = TEMImage(file)
        fig = plt.figure(figsize=(6,6))
        plt.imshow(img.z, cmap='Greys_r', origin='lower', aspect='equal')
        ax = plt.gca()
        img.set_xy_ticks(ax)
        img.show_auto_scale_bar(ax, (0.1, 0.1), color='white', lw=2, fontsize=12, text_y_offset=0.025)
        plt.tight_layout()
        if args.save:
            plt.savefig('.'.join(file.split('.')[:-1])+'.'+args.extension, bbox_inches='tight')
    if args.save == False:
        plt.show()

if __name__ == '__main__':
    main()