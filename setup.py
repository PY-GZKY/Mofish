from setuptools import setup, find_packages

description = '你好，摸鱼人，工作再累，一定不要忘记摸鱼哦! 有事没事起身去茶水间去廊道去天台走走，别老在工位上坐着。多喝点水，钱是老板的，但命是自己的!'

setup(
    name='mofish',
    version='1.0.2',
    description=description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Framework :: AsyncIO',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Clustering',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Systems Administration',
    ],
    python_requires='>=3.6',
    author='PY-GZKY',
    author_email='341796767@qq.com',
    url='https://github.com/PY-GZKY/Moyu_',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    entry_points="""
        [console_scripts]
        moyu=src.main:cli
    """,
    install_requires=[
        'click>=6.7',
        'zhdate'
    ],

)
